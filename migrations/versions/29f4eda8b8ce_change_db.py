"""change db

Revision ID: 29f4eda8b8ce
Revises: 14395d572785
Create Date: 2024-08-11 09:05:55.923693

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '29f4eda8b8ce'
down_revision: Union[str, None] = '14395d572785'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('position', sa.Column('user_id', sa.BigInteger(), nullable=True))
    op.create_foreign_key(None, 'position', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.add_column('property', sa.Column('user_id', sa.BigInteger(), nullable=True))
    op.create_foreign_key(None, 'property', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.add_column('record', sa.Column('user_id', sa.BigInteger(), nullable=True))
    op.create_foreign_key(None, 'record', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'record', type_='foreignkey')
    op.drop_column('record', 'user_id')
    op.drop_constraint(None, 'property', type_='foreignkey')
    op.drop_column('property', 'user_id')
    op.drop_constraint(None, 'position', type_='foreignkey')
    op.drop_column('position', 'user_id')
    # ### end Alembic commands ###
