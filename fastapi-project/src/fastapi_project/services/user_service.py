from fastapi_project.models.users import User
from fastapi_project.repositories.user_repository import UserRepository
from fastapi_project.schemas.user import CreateUser


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_users(self):
        return self.user_repository.get_all()

    def get_user(self, user_id: int):
        return self.user_repository.get_by_id(user_id)

    def create_user(self, user_data: CreateUser):
        return self.user_repository.create(user_data)

    def update_user(self, user_id: int, user_data: CreateUser):
        return self.user_repository.update(user_id, user_data)

    def delete_user(self, user_id: int):
        return self.user_repository.delete(user_id)