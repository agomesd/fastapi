"""Add content column to posts

Revision ID: e00a9e8eca58
Revises: 7955d40ab0c2
Create Date: 2022-01-04 16:45:43.119302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e00a9e8eca58"
down_revision = "7955d40ab0c2"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
