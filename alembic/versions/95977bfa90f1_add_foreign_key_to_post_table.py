"""add foreign key to post table

Revision ID: 95977bfa90f1
Revises: cf6a9422f954
Create Date: 2022-01-04 16:59:16.531885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "95977bfa90f1"
down_revision = "cf6a9422f954"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
