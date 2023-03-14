"""add last few columns to posts table

Revision ID: 515014b9937e
Revises: ca32d9e5d1aa
Create Date: 2023-03-12 20:07:51.923368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '515014b9937e'
down_revision = 'ca32d9e5d1aa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
