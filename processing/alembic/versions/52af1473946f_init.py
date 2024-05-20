"""init

Revision ID: 52af1473946f
Revises:
Create Date: 2022-05-18 14:46:07.845635

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "52af1473946f"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "preprocessing_tasks",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("execution_id", sa.Integer(), nullable=True),
        sa.Column("chunk_id", sa.String(length=100), nullable=True),
        sa.Column("file_id", sa.Integer(), nullable=False),
        sa.Column("pipeline_id", sa.Integer(), nullable=False),
        sa.Column("status", sa.String(length=100), nullable=True),
        sa.Column("execution_args", sa.JSON(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("preprocessing_tasks")
    # ### end Alembic commands ###
