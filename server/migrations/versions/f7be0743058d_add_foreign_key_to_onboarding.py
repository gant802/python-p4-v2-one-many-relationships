"""add foreign key to onboarding

Revision ID: f7be0743058d
Revises: 6de7b7a45e5c
Create Date: 2024-06-03 11:01:42.005041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7be0743058d'
down_revision = '6de7b7a45e5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('onboardings', sa.Column('employee_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_onboardings_employee_id_employees'), 'onboardings', 'employees', ['employee_id'], ['id'])
    op.create_foreign_key(op.f('fk_reviews_employee_id_employees'), 'reviews', 'employees', ['employee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_reviews_employee_id_employees'), 'reviews', type_='foreignkey')
    op.drop_constraint(op.f('fk_onboardings_employee_id_employees'), 'onboardings', type_='foreignkey')
    op.drop_column('onboardings', 'employee_id')
    # ### end Alembic commands ###
