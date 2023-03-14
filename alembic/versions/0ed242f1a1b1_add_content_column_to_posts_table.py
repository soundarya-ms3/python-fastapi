"""add content column to posts table

Revision ID: 0ed242f1a1b1
Revises: 51efe880e370
Create Date: 2023-03-12 19:32:27.948363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ed242f1a1b1'
down_revision = '51efe880e370'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
