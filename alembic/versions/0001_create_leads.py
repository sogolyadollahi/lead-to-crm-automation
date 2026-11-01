"""Create leads table.

Revision ID: 0001_create_leads
Revises:
Create Date: 2026-11-02
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "0001_create_leads"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "leads",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("full_name", sa.String(length=120), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column("phone", sa.String(length=30), nullable=True),
        sa.Column("company", sa.String(length=150), nullable=True),
        sa.Column("source", sa.String(length=100), nullable=True),
        sa.Column(
            "status",
            sa.String(length=20),
            server_default="new",
            nullable=False,
        ),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.CheckConstraint(
            "status IN ('new', 'contacted', 'qualified', 'converted', 'lost')",
            name="ck_leads_status",
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email", name="uq_leads_email"),
    )
    op.create_index("ix_leads_status", "leads", ["status"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_leads_status", table_name="leads")
    op.drop_table("leads")
