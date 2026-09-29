from sqlalchemy import select
from sqlalchemy.orm import Session

from fastapi_project.models.users import User
from fastapi_project.schemas.user import CreateUser


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        result = self.db.execute(select(User))
        return list(result.scalars().all())

    def get_by_id(self, user_id: int):
        return self.db.get(User, user_id)

    def create(self, user_data: CreateUser):
        user = User(name=user_data.name, email=user_data.email)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update(self, user_id: int, user_data: CreateUser):
        user = self.get_by_id(user_id)
        if user is None:
            return None

        user.name = user_data.name
        user.email = user_data.email
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, user_id: int):
        user = self.get_by_id(user_id)
        if user is None:
            return False

        self.db.delete(user)
        self.db.commit()
        return True