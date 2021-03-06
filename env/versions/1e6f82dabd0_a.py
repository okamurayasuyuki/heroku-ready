"""a

Revision ID: 1e6f82dabd0
Revises: 36345ef3227
Create Date: 2014-02-15 20:41:26.040337

"""

# revision identifiers, used by Alembic.
revision = '1e6f82dabd0'
down_revision = '36345ef3227'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    op.drop_constraint('users_password_key', 'users')
    op.drop_index('users_password_key', table_name='users')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index('users_password_key', 'users', ['password'], unique=True)
    op.create_unique_constraint('users_password_key', 'users', ['password'])
    op.add_column('users', sa.Column('password', sa.VARCHAR(length=80), nullable=True))
    ### end Alembic commands ###
