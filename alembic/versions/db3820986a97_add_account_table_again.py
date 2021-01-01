"""add account table again

Revision ID: db3820986a97
Revises: c313b29d80e1
Create Date: 2021-01-01 13:25:16.911386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db3820986a97'
down_revision = 'c313b29d80e1'
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
