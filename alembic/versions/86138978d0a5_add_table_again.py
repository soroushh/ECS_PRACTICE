"""add table again

Revision ID: 86138978d0a5
Revises: 47a00c1e5f05
Create Date: 2021-03-26 12:46:19.618627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86138978d0a5'
down_revision = '47a00c1e5f05'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )


def downgrade():
    op.drop_table('account')
