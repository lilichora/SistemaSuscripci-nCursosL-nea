"""Initial migration

Revision ID: afcd7c25c250
Revises: 8e17d84f8978
Create Date: 2024-11-22 07:49:18.722178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afcd7c25c250'
down_revision = '8e17d84f8978'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'courses', 'users', ['creator_id'], ['id'])
    op.create_foreign_key(None, 'subscriptions', 'courses', ['course_id'], ['id'])
    op.create_foreign_key(None, 'subscriptions', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'subscriptions', type_='foreignkey')
    op.drop_constraint(None, 'subscriptions', type_='foreignkey')
    op.drop_constraint(None, 'courses', type_='foreignkey')
    # ### end Alembic commands ###
