"""add blacklist table

Revision ID: 71eb813bc37c
Revises: f1593b7c06ab
Create Date: 2021-03-25 05:34:30.344378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71eb813bc37c'
down_revision = 'f1593b7c06ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_token',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blacklist_token')
    # ### end Alembic commands ###