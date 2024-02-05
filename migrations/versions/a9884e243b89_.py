"""empty message

Revision ID: a9884e243b89
Revises: f4480545e245
Create Date: 2024-02-01 18:56:52.346712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9884e243b89'
down_revision = 'f4480545e245'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('adoption_users', schema=None) as batch_op:
        batch_op.drop_constraint('adoption_users_testimony_id_key', type_='unique')
        batch_op.drop_constraint('adoption_users_testimony_id_fkey', type_='foreignkey')
        batch_op.drop_column('testimony_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('adoption_users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('testimony_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('adoption_users_testimony_id_fkey', 'testimony', ['testimony_id'], ['id'])
        batch_op.create_unique_constraint('adoption_users_testimony_id_key', ['testimony_id'])

    # ### end Alembic commands ###