from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from fastapi_project.models.departments import Department
    from fastapi_project.models.user_profiles import UserProfile


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    department_id: Mapped[int | None] = mapped_column(
        ForeignKey("departments.id"),
        nullable=True,
    )
    department: Mapped["Department | None"] = relationship(
        back_populates="users",
    )
    
    profile: Mapped["UserProfile | None"] = relationship(
        back_populates="user",
        uselist=False,
    )