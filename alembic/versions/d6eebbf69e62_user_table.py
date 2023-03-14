""" user table

Revision ID: d6eebbf69e62
Revises: 0ed242f1a1b1
Create Date: 2023-03-12 19:47:29.512803

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6eebbf69e62'
down_revision = '0ed242f1a1b1'
branch_labels = None
depends_on = None


def upgrade() -> None:
        op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
        pass


def downgrade() -> None:
    op.drop_table('users')
    pass
