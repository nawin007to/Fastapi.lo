from fastapi import APIRouter,HTTPException
from sqlmodel import select
from .database import SessionDep
from .model import Employee
from .schema import EmployeeCreate, EmployeeResponse

router = APIRouter(tags=["employees"])


@router.post("/employees", response_model=EmployeeResponse, status_code=201)
def create_employee(employee: EmployeeCreate, session: SessionDep):
    db_employee = Employee.model_validate(employee)
    session.add(db_employee)
    session.commit()
    session.refresh(db_employee)
    return db_employee

@router.get("/employees/{emp_id}",response_model=EmployeeResponse)
def get_employee(emp_id:int,session:SessionDep):
    db_employee = session.get(Employee,emp_id)
    if not db_employee:
        raise HTTPException(status_code=404,detail="Employee not found")
    return db_employee

@router.get("/employees", response_model=list[EmployeeResponse])
def get_employees(session:SessionDep):
    db_employee = session.exec(select(Employee)).all()
    return db_employee
