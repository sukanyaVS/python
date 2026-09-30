from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from fastapi_project.models.user_profiles import UserProfile
from fastapi_project.models.users import User
from fastapi_project.schemas.user import CreateUser


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        result = await self.db.execute(
            select(User).options(
                selectinload(User.department),
                selectinload(User.profile),
            )
        )
        return list(result.scalars().all())

    async def get_by_id(self, user_id: int):
        result = await self.db.execute(
            select(User)
            .where(User.id == user_id)
            .options(
                selectinload(User.department),
                selectinload(User.profile),
            )
        )
        return result.scalar_one_or_none()

    async def create(self, user_data: CreateUser):
        user_fields = user_data.model_dump(exclude={"profile"})
        profile_data = user_data.profile
        user = User(
            **user_fields,
            profile=(
                UserProfile(**profile_data.model_dump())
                if profile_data is not None
                else None
            ),
        )
        self.db.add(user)
        await self.db.commit()
        return await self.get_by_id(user.id)

    async def update(self, user_id: int, user_data: CreateUser):
        user = await self.get_by_id(user_id)
        if user is None:
            return None

        user.name = user_data.name
        user.email = user_data.email
        user.department_id = user_data.department_id
        await self.db.commit()
        return await self.get_by_id(user_id)

    async def delete(self, user_id: int):
        user = await self.get_by_id(user_id)
        if user is None:
            return False

        await self.db.delete(user)
        await self.db.commit()
        return True