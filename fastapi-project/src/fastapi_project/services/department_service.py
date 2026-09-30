from fastapi_project.repositories.department_repository import DepartmentRepository
from fastapi_project.schemas.department import CreateDepartment


class DepartmentService:
    def __init__(self, department_repository: DepartmentRepository):
        self.department_repository = department_repository

    async def get_department(self, department_id: int):
        return await self.department_repository.get_by_id(department_id)

    async def create_department(self, department_data: CreateDepartment):
        return await self.department_repository.create(department_data)