"""followers

Revision ID: 2babda0b2099
Revises: 185a4a2c7842
Create Date: 2018-07-26 15:48:05.500318

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2babda0b2099'
down_revision = '185a4a2c7842'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
