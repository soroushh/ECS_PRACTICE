"""create useless account table.

Revision ID: d803b1fdc27e
Revises: fce406fbd054
Create Date: 2020-12-30 17:47:38.629156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd803b1fdc27e'
down_revision = 'fce406fbd054'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('account')


def downgrade():
    pass
