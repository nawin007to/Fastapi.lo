from sqlmodel import Field, SQLModel


class EmployeeBase(SQLModel):
    name: str = Field(min_length=1)
    age: int = Field(ge=0)
    position: str = Field(min_length=1)
    gender: str | None = None


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(SQLModel):
    name: str | None = Field(default=None, min_length=1)
    age: int | None = Field(default=None, ge=0)
    position: str | None = Field(default=None, min_length=1)
    gender: str | None = None


class EmployeeResponse(EmployeeBase):
    id: int
