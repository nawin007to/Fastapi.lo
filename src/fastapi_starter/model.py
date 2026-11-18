"""SQLModel table definitions."""

from sqlmodel import Field, SQLModel


class Employee(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(min_length=1)
    age: int
    position: str = Field(min_length=1)
    gender: str | None = None
