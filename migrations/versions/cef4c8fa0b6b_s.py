"""s

Revision ID: cef4c8fa0b6b
Revises: c317e1e1cb9d
Create Date: 2023-08-14 20:30:21.449109

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cef4c8fa0b6b'
down_revision = 'c317e1e1cb9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user3',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=200), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user2')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user2',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('user3')
    # ### end Alembic commands ###
