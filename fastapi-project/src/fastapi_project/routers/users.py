from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_project.database import get_db
from fastapi_project.repositories.user_repository import UserRepository
from fastapi_project.schemas.user import CreateUser, CreateUserResponse
from fastapi_project.schemas.user import CreateUser, UserResponse
from fastapi_project.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


def get_user_service(db: AsyncSession = Depends(get_db)):
    return UserService(UserRepository(db))


@router.get("/")
async def get_users(service: UserService = Depends(get_user_service)):
    return await service.get_users()

@router.post("/", response_model=CreateUserResponse)
@router.post("/", response_model=UserResponse)
async def create_user(user: CreateUser, service: UserService = Depends(get_user_service)):
    return await service.create_user(user)


@router.get("/{user_id}", response_model=CreateUserResponse)
@router.get("/{user_id}", response_model=UserResponse)
    response_model=UserResponse,
async def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    user = await service.get_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user


@router.put("/{user_id}", response_model=CreateUserResponse)
async def update_user(
    user_id: int,
    updated_user: CreateUser,
    service: UserService = Depends(get_user_service),
):
    user = await service.update_user(user_id, updated_user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user

@router.delete("/{user_id}")
async def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    deleted = await service.delete_user(user_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return {"message": "User deleted successfully"}    