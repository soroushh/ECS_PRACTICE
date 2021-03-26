"""delete added table

Revision ID: 756d54972dad
Revises: 86138978d0a5
Create Date: 2021-03-26 14:17:14.369097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '756d54972dad'
down_revision = '86138978d0a5'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('account')


def downgrade():
    pass
