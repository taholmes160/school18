"""add grade and age to student profile model

Revision ID: 891b145a704e
Revises: 82cf1b4d8900
Create Date: 2024-10-14 18:20:23.329521

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
from sqlalchemy import inspect

# revision identifiers, used by Alembic.
revision = '891b145a704e'
down_revision = '82cf1b4d8900'
branch_labels = None
depends_on = None


def upgrade():
    # Reflect the table to check if the 'user_id', 'grade', and 'age' columns exist
    conn = op.get_bind()
    inspector = inspect(conn)
    columns = [col['name'] for col in inspector.get_columns('student_profiles')]

    with op.batch_alter_table('student_profiles', schema=None) as batch_op:
        if 'user_id' not in columns:
            batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        if 'grade' not in columns:
            batch_op.add_column(sa.Column('grade', sa.String(length=64), nullable=True))
        if 'age' not in columns:
            batch_op.add_column(sa.Column('age', sa.Integer(), nullable=True))
        if 'user_id' not in columns:
            batch_op.create_foreign_key('fk_student_profiles_user_id', 'users', ['user_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=mysql.VARCHAR(length=512),
               type_=sa.String(length=512),
               existing_nullable=False)
        batch_op.drop_column('password_reset_expiration')
        batch_op.drop_column('login_attempts')
        batch_op.drop_column('is_admin')
        batch_op.drop_column('deactivated_at')
        batch_op.drop_column('phone_number')
        batch_op.drop_column('last_login_at')
        batch_op.drop_column('timezone')
        batch_op.drop_column('bio')
        batch_op.drop_column('language')
        batch_op.drop_column('is_active')
        batch_op.drop_column('password_reset_token')


def downgrade():
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_reset_token', mysql.VARCHAR(length=128), nullable=True))
        batch_op.add_column(sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('language', mysql.VARCHAR(length=64), nullable=True))
        batch_op.add_column(sa.Column('bio', mysql.TEXT(), nullable=True))
        batch_op.add_column(sa.Column('timezone', mysql.VARCHAR(length=64), nullable=True))
        batch_op.add_column(sa.Column('last_login_at', mysql.DATETIME(), nullable=True))
        batch_op.add_column(sa.Column('phone_number', mysql.VARCHAR(length=20), nullable=True))
        batch_op.add_column(sa.Column('deactivated_at', mysql.DATETIME(), nullable=True))
        batch_op.add_column(sa.Column('is_admin', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('login_attempts', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('password_reset_expiration', mysql.DATETIME(), nullable=True))
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=512),
               type_=mysql.VARCHAR(length=512),
               existing_nullable=False)

    with op.batch_alter_table('student_profiles', schema=None) as batch_op:
        batch_op.drop_constraint('fk_student_profiles_user_id', type_='foreignkey')
        batch_op.drop_column('age')
        batch_op.drop_column('grade')
        batch_op.drop_column('user_id')
