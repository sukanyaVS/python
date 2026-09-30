from pydantic import BaseModel

from fastapi_project.schemas.user import UserResponse


class CreateDepartment(BaseModel):
    name: str


class DepartmentResponse(BaseModel):
    id: int
    name: str
    users: list[UserResponse]

    model_config = {"from_attributes": True}