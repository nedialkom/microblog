"""new fields in user model

Revision ID: 185a4a2c7842
Revises: 220dc2f359e9
Create Date: 2018-07-26 12:16:47.014453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '185a4a2c7842'
down_revision = '220dc2f359e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
