"""add due

Revision ID: 56e1a7f9aacb
Revises: c9b0122a16d
Create Date: 2015-03-05 14:48:48.371373

"""

# revision identifiers, used by Alembic.
revision = '56e1a7f9aacb'
down_revision = 'c9b0122a16d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'due',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('purchase_id', sa.Integer(), nullable=False, index=True),
        sa.Column('amount', sa.Float(), nullable=False),
        sa.Column('status', sa.String(64), nullable=False, index=True),
        sa.Column('date_created', sa.DateTime(timezone=True),
                  nullable=False, index=True,
                  server_default=sa.func.current_timestamp()),
        sa.Column('date_updated', sa.DateTime(timezone=True),
                  nullable=False, index=True,
                  server_default=sa.func.current_timestamp())
    )


def downgrade():
    op.drop_table('due')
