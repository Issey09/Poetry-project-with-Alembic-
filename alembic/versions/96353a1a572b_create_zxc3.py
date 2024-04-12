"""Create zxc3

Revision ID: 96353a1a572b
Revises: 4dc821966706
Create Date: 2024-04-11 23:38:07.604757

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "96353a1a572b"
down_revision: Union[str, None] = "4dc821966706"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_users_czxc", table_name="users")
    op.drop_index("ix_users_email", table_name="users")
    op.drop_index("ix_users_nickname", table_name="users")
    op.drop_index("ix_users_password", table_name="users")
    op.drop_table("users")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("nickname", sa.VARCHAR(), nullable=True),
        sa.Column("password", sa.VARCHAR(), nullable=True),
        sa.Column("email", sa.VARCHAR(), nullable=True),
        sa.Column("create_at", sa.DATETIME(), nullable=True),
        sa.Column("czxc", sa.VARCHAR(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_users_password", "users", ["password"], unique=False)
    op.create_index("ix_users_nickname", "users", ["nickname"], unique=False)
    op.create_index("ix_users_email", "users", ["email"], unique=False)
    op.create_index("ix_users_czxc", "users", ["czxc"], unique=False)
    # ### end Alembic commands ###
