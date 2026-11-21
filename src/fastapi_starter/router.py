from fastapi import APIRouter,HTTPException
from sqlmodel import select
from .database import SessionDep
from .model import Employee
from .schema import EmployeeCreate, EmployeeResponse,EmployeeUpdate

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

@router.put("/employees/{emp_id}",response_model=EmployeeResponse)
def put_employee(emp_id:int,update:EmployeeUpdate,session:SessionDep):
    db_employee = session.get(Employee,emp_id)
    if not db_employee:
        raise HTTPException(status_code=404,detail="Employee not found")
    data = update.model_dump(exclude_unset=True)
    db_employee.sqlmodel_update(data)
    session.add(db_employee)
    session.commit()
    session.refresh(db_employee)
    return db_employee

@router.delete("/employees/{emp_id}")
def delete_employee(emp_id:int, session:SessionDep):
    data = session.get(Employee,emp_id)
    if not data:
        raise HTTPException(status_code=404,detail="Employee not found")
    session.delete(data)
    session.commit()
    return {"message": "ลบเสร็จเรียบร้อย"}