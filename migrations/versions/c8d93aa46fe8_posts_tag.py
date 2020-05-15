"""posts tag

Revision ID: c8d93aa46fe8
Revises: 7040ce8985c8
Create Date: 2020-03-18 19:11:48.214433

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8d93aa46fe8'
down_revision = '7040ce8985c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_softwares_dateRelease'), 'softwares', ['dateRelease'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_softwares_dateRelease'), table_name='softwares')
    # ### end Alembic commands ###