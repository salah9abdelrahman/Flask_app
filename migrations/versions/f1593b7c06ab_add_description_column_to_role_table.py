"""add description column to role table

Revision ID: f1593b7c06ab
Revises: 89401af6e907
Create Date: 2021-03-25 04:19:17.296430

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1593b7c06ab'
down_revision = '89401af6e907'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('role', sa.Column('description', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('role', 'description')
    # ### end Alembic commands ###
