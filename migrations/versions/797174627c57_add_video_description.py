"""ADd video description

Revision ID: 797174627c57
Revises: d804a3be0d84
Create Date: 2021-11-29 19:46:34.577108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '797174627c57'
down_revision = 'd804a3be0d84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('video', 'description')
    # ### end Alembic commands ###
