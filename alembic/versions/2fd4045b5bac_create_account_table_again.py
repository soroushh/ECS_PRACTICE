"""Create account table again.

Revision ID: 2fd4045b5bac
Revises: d803b1fdc27e
Create Date: 2020-12-31 10:20:10.192570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fd4045b5bac'
down_revision = 'd803b1fdc27e'
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
