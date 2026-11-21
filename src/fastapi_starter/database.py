"""SQLite database engine and session dependency."""
from typing import Annotated
from pathlib import Path
from collections.abc import Generator
from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine


DATABASE_FILE = Path(__file__).resolve().parents[2] / "database.db"
DATABASE_URL = f"sqlite:///{DATABASE_FILE.as_posix()}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)


def create_db_and_tables() -> None:
    from . import model  
    with engine.connect() as connection:
        SQLModel.metadata.create_all(connection)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
SessionDep = Annotated[Session,Depends(get_session)]