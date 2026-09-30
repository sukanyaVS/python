from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_project.database import get_db
from fastapi_project.repositories.department_repository import DepartmentRepository
from fastapi_project.schemas.department import CreateDepartment, DepartmentResponse
from fastapi_project.services.department_service import DepartmentService

router = APIRouter(prefix="/departments", tags=["Departments"])


def get_department_service(db: AsyncSession = Depends(get_db)):
    return DepartmentService(DepartmentRepository(db))


@router.post("/", response_model=DepartmentResponse, status_code=status.HTTP_201_CREATED)
async def create_department(
    department: CreateDepartment,
    service: DepartmentService = Depends(get_department_service),
):
    return await service.create_department(department)


@router.get("/{department_id}", response_model=DepartmentResponse)
async def get_department(
    department_id: int,
    service: DepartmentService = Depends(get_department_service),
):
    department = await service.get_department(department_id)
    if department is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Department not found",
        )
    return department