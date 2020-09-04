"""update

Revision ID: 2d37229f23db
Revises: 673ce29f85d2
Create Date: 2020-08-22 15:10:44.269332

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d37229f23db'
down_revision = '673ce29f85d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categories')
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.add_column(sa.Column('software_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('timestamp', sa.DateTime(), nullable=True))
        batch_op.create_index(batch_op.f('ix_category_timestamp'), ['timestamp'], unique=False)
        batch_op.create_foreign_key(batch_op.f('fk_category_software_id_software'), 'software', ['software_id'], ['id'])

    with op.batch_alter_table('source', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sa.String(length=200), nullable=True))
        batch_op.create_index(batch_op.f('ix_source_category'), ['category'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('source', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_source_category'))
        batch_op.drop_column('category')

    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_category_software_id_software'), type_='foreignkey')
        batch_op.drop_index(batch_op.f('ix_category_timestamp'))
        batch_op.drop_column('timestamp')
        batch_op.drop_column('software_id')

    op.create_table('categories',
    sa.Column('category_id', sa.INTEGER(), nullable=False),
    sa.Column('source_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], name='fk_categories_category_id_category'),
    sa.ForeignKeyConstraint(['source_id'], ['source.id'], name='fk_categories_source_id_source'),
    sa.PrimaryKeyConstraint('category_id', 'source_id', name='pk_categories')
    )
    # ### end Alembic commands ###