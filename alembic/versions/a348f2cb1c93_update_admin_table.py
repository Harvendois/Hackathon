"""update admin table

Revision ID: a348f2cb1c93
Revises: c664c61aea2d
Create Date: 2024-04-27 10:58:10.509718

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "a348f2cb1c93"
down_revision: Union[str, None] = "c664c61aea2d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("admins", "name")
    op.drop_column("admins", "email")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "admins", sa.Column("email", sa.VARCHAR(), autoincrement=False, nullable=False)
    )
    op.add_column(
        "admins", sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=False)
    )
    # ### end Alembic commands ###
