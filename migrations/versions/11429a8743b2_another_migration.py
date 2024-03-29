"""another migration

Revision ID: 11429a8743b2
Revises: a15f68bc8e2f
Create Date: 2024-01-31 21:02:50.828239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11429a8743b2'
down_revision = 'a15f68bc8e2f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('review_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('stadium_id', sa.Integer(), nullable=False),
    sa.Column('user_submitted', sa.String(length=50), nullable=False),
    sa.Column('review_text', sa.Text(), nullable=False),
    sa.Column('review_stars', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('review_id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), nullable=False))

    op.drop_table('reviews')
    # ### end Alembic commands ###
