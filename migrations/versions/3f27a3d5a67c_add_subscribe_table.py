"""add subscribe table

Revision ID: 3f27a3d5a67c
Revises: 8b976517bfcc
Create Date: 2019-03-04 12:21:50.015156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f27a3d5a67c'
down_revision = '8b976517bfcc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subs_email'), 'subs', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_subs_email'), table_name='subs')
    op.drop_table('subs')
    # ### end Alembic commands ###
