from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from fastapi_project.database import get_db
from fastapi_project.models import User
from fastapi_project.schemas.user import CreateUser, CreateUserResponse

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/")
def get_users(db: Session = Depends(get_db)):
    result = db.execute(select(User))
    users = result.scalars().all()

    return users

@router.post("/", response_model=CreateUserResponse)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    new_user = User(
        name=user.name,
        email=user.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{user_id}", response_model=CreateUserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user


@router.put("/{user_id}", response_model=CreateUserResponse)
def update_user(user_id: int, updated_user: CreateUser, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    user.name = updated_user.name
    user.email = updated_user.email
    db.commit()
    db.refresh(user)
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}    