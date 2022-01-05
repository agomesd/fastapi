"""Create Posts Table

Revision ID: 7955d40ab0c2
Revises:
Create Date: 2022-01-04 16:35:18.535641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7955d40ab0c2"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade():
    op.drop_table("posts")
    pass
