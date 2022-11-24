"""new_models_and_relations

Revision ID: 0c31de437a89
Revises: 91bb01f49649
Create Date: 2022-11-24 21:28:32.875030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c31de437a89'
down_revision = '91bb01f49649'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courses',
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['department_id'], ['departments.id'], ),
    sa.PrimaryKeyConstraint('course_id')
    )
    op.create_table('student_grades',
    sa.Column('enrollment_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('grade', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.course_id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('enrollment_id')
    )
    op.create_foreign_key(None, 'online_courses', 'courses', ['id'], ['course_id'])
    op.create_foreign_key(None, 'onside_courses', 'courses', ['id'], ['course_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'onside_courses', type_='foreignkey')
    op.drop_constraint(None, 'online_courses', type_='foreignkey')
    op.drop_table('student_grades')
    op.drop_table('courses')
    # ### end Alembic commands ###
