"""remove account table

Revision ID: c313b29d80e1
Revises: 25ce5c1043bd
Create Date: 2020-12-31 14:08:17.464755

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c313b29d80e1'
down_revision = '25ce5c1043bd'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('account')


def downgrade():
    pass
