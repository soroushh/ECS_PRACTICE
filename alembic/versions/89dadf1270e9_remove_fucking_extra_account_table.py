"""remove fucking extra account table.

Revision ID: 89dadf1270e9
Revises: 2fd4045b5bac
Create Date: 2020-12-31 11:04:37.191196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89dadf1270e9'
down_revision = '2fd4045b5bac'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('account')


def downgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )
