from sqlmodel import SQLModel 

class Employee(SQLModel):
    name : str
    age : int
    position :str
    gender: str
