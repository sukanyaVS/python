from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from fastapi_project.models.users import Base

if TYPE_CHECKING:
    from fastapi_project.models.users import User


class UserProfile(Base):
    __tablename__ = "user_profiles"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
    )

    phone: Mapped[str | None]
    address: Mapped[str | None]

    user: Mapped["User"] = relationship(
        back_populates="profile",
        uselist=False,
    )