"""added workoutplan

Revision ID: 10d57dfabe8a
Revises: 653167b6738f
Create Date: 2020-10-07 19:44:25.759617

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10d57dfabe8a'
down_revision = '653167b6738f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('workoutplan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('add', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_workoutplan_add'), 'workoutplan', ['add'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_workoutplan_add'), table_name='workoutplan')
    op.drop_table('workoutplan')
    # ### end Alembic commands ###
