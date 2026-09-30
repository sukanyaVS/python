from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from fastapi_project.models.departments import Department
from fastapi_project.models.users import User
from fastapi_project.schemas.department import CreateDepartment


class DepartmentRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, department_id: int):
        result = await self.db.execute(
            select(Department)
            .where(Department.id == department_id)
            .options(
                selectinload(Department.users).selectinload(User.profile),
                selectinload(Department.users).selectinload(User.department),
            )
        )
        return result.scalar_one_or_none()

    async def create(self, department_data: CreateDepartment):
        department = Department(name=department_data.name)
        self.db.add(department)
        await self.db.commit()
        return await self.get_by_id(department.id)