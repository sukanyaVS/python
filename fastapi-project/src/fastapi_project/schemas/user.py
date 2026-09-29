from pydantic import BaseModel

class CreateUser(BaseModel):
    name: str
    email: str


class CreateUserResponse(BaseModel):
    id: int
    name: str
    email: str

    model_config = {
        "from_attributes": True
    }   