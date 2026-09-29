from fastapi_project.models.users import User
from fastapi_project.repositories.user_repository import UserRepository
from fastapi_project.schemas.user import CreateUser


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def get_users(self):
        users = await self.user_repository.get_all()
        return users

    async def get_user(self, user_id: int):
        return await self.user_repository.get_by_id(user_id)

    async def create_user(self, user_data: CreateUser):
        return await self.user_repository.create(user_data)

    async def update_user(self, user_id: int, user_data: CreateUser):
        return await self.user_repository.update(user_id, user_data)

    async def delete_user(self, user_id: int):
        return await self.user_repository.delete(user_id)