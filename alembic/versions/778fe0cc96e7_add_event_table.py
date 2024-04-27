"""add event table

Revision ID: 778fe0cc96e7
Revises: 46608a2f0976
Create Date: 2024-04-27 15:02:47.330079

"""

from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "778fe0cc96e7"
down_revision: Union[str, None] = "46608a2f0976"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "events",
        sa.Column("event_type", sa.String(), nullable=False),
        sa.Column("school_type", sa.String(), nullable=True),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("start_dt", postgresql.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("end_dt", postgresql.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("venue", sa.String(), nullable=False),
        sa.Column("details", sa.String(), nullable=False),
        sa.Column("contact_info", sa.String(), nullable=False),
        sa.Column("rsvp_info", sa.String(), nullable=True),
        sa.Column("poster", sa.String(), nullable=False),
        sa.Column(
            "verified", sa.Boolean(), server_default=sa.text("false"), nullable=False
        ),
        sa.Column(
            "id", sa.UUID(), server_default=sa.text("gen_random_uuid()"), nullable=False
        ),
        sa.Column(
            "create_dt",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("update_dt", postgresql.TIMESTAMP(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("events")
    # ### end Alembic commands ###