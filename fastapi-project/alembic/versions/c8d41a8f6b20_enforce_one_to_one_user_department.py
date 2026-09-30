"""enforce one-to-one user department relation

Revision ID: c8d41a8f6b20
Revises: fd582feff879
Create Date: 2026-09-29

"""
from typing import Sequence, Union

from alembic import op


revision: str = "c8d41a8f6b20"
down_revision: Union[str, Sequence[str], None] = "fd582feff879"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint(
        "uq_users_department_id",
        "users",
        ["department_id"],
    )


def downgrade() -> None:
    op.drop_constraint("uq_users_department_id", "users", type_="unique")