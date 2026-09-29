from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_project.models.users import User
from fastapi_project.schemas.user import CreateUser


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        result = await self.db.execute(select(User))
        return list(result.scalars().all())

    async def get_by_id(self, user_id: int):
        return await self.db.get(User, user_id)

    async def create(self, user_data: CreateUser):
        user = User(name=user_data.name, email=user_data.email)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def update(self, user_id: int, user_data: CreateUser):
        user = await self.get_by_id(user_id)
        if user is None:
            return None

        user.name = user_data.name
        user.email = user_data.email
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def delete(self, user_id: int):
        user = await self.get_by_id(user_id)
        if user is None:
            return False

        await self.db.delete(user)
        await self.db.commit()
        return True