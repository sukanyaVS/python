from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from fastapi_project.models.users import Base

if TYPE_CHECKING:
    from fastapi_project.models.users import User


class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    users: Mapped[list["User"]] = relationship(
        back_populates="department",
    )