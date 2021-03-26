"""add user table

Revision ID: 9f5fb6fb4ec7
Revises: 756d54972dad
Create Date: 2021-03-26 15:52:22.701129

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f5fb6fb4ec7'
down_revision = '756d54972dad'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('email', sa.Unicode(200)),
    )

def downgrade():
    op.drop_table('users')
