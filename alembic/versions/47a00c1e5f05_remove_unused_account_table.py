"""remove unused account table.

Revision ID: 47a00c1e5f05
Revises: db3820986a97
Create Date: 2021-01-01 21:10:34.180883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47a00c1e5f05'
down_revision = 'db3820986a97'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('account')


def downgrade():
    pass
