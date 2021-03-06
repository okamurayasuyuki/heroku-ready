"""add age

Revision ID: 54c66664bdd
Revises: 2950b44eedc
Create Date: 2014-02-15 20:46:07.489827

"""

# revision identifiers, used by Alembic.
revision = '54c66664bdd'
down_revision = '2950b44eedc'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('age', sa.String(length=80), nullable=True))
    op.create_unique_constraint(None, 'users', ['age'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users')
    op.drop_column('users', 'age')
    ### end Alembic commands ###
