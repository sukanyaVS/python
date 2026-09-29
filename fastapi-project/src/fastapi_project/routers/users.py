from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from fastapi_project.database import get_db
from fastapi_project.repositories.user_repository import UserRepository
from fastapi_project.schemas.user import CreateUser, CreateUserResponse
from fastapi_project.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(UserRepository(db))


@router.get("/")
def get_users(service: UserService = Depends(get_user_service)):
    return service.get_users()

@router.post("/", response_model=CreateUserResponse)
def create_user(user: CreateUser, service: UserService = Depends(get_user_service)):
    return service.create_user(user)


@router.get("/{user_id}", response_model=CreateUserResponse)
def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    user = service.get_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user


@router.put("/{user_id}", response_model=CreateUserResponse)
def update_user(
    user_id: int,
    updated_user: CreateUser,
    service: UserService = Depends(get_user_service),
):
    user = service.update_user(user_id, updated_user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    deleted = service.delete_user(user_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return {"message": "User deleted successfully"}    