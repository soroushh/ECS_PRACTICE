"""create account table again.

Revision ID: 25ce5c1043bd
Revises: 89dadf1270e9
Create Date: 2020-12-31 11:26:20.281344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25ce5c1043bd'
down_revision = '89dadf1270e9'
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
