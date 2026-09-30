from pydantic import BaseModel

class CreateUser(BaseModel):
    name: str
    email: str
    department_id: int | None = None
    profile: CreateProfile | None = None


class ProfileResponse(BaseModel):
    id: int
    phone: str | None
    address: str | None

    model_config = {"from_attributes": True}


class DepartmentSummary(BaseModel):
    id: int
    name: str

    model_config = {"from_attributes": True}


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    department_id: int | None
    department: DepartmentSummary | None
    profile: ProfileResponse | None

    model_config = {
        "from_attributes": True
    }