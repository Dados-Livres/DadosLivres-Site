"""atualizei software

Revision ID: 23921936f8ef
Revises: 390a0aa7f540
Create Date: 2020-03-22 01:07:03.680127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23921936f8ef'
down_revision = '390a0aa7f540'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'typeUser')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('typeUser', sa.VARCHAR(length=200), nullable=True))
    # ### end Alembic commands ###
