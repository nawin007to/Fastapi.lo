"""SQLite database engine and session dependency."""

from pathlib import Path
from collections.abc import Generator

from sqlmodel import Session, SQLModel, create_engine


DATABASE_FILE = Path(__file__).resolve().parents[2] / "database.db"
DATABASE_URL = f"sqlite:///{DATABASE_FILE.as_posix()}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)


def create_db_and_tables() -> None:
    """Create the SQLite file and any registered SQLModel tables."""
    from . import model  # noqa: F401 — registers table models with SQLModel metadata

    with engine.connect() as connection:
        SQLModel.metadata.create_all(connection)


def get_session() -> Generator[Session, None, None]:
    """Provide a database session to a FastAPI endpoint."""
    with Session(engine) as session:
        yield session
