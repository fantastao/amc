"""init

Revision ID: c9b0122a16d
Revises: None
Create Date: 2014-12-09 13:26:04.799675

"""

# revision identifiers, used by Alembic.
revision = 'c9b0122a16d'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'auth',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('account', sa.String(64), nullable=False, unique=True),
        sa.Column('pw_hash', sa.String(256), nullable=False),
        sa.Column('is_verified', sa.Boolean(), nullable=False,
                  server_default=sa.sql.false()),
        sa.Column('date_created', sa.DateTime(timezone=True), nullable=False,
                  server_default=sa.func.current_timestamp())
    )
    op.create_table(
        'order',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), nullable=False, index=True),
        sa.Column('status', sa.String(64), nullable=False, index=True),
        sa.Column('date_created', sa.DateTime(timezone=True),
                  nullable=False, index=True,
                  server_default=sa.func.current_timestamp()),
        sa.Column('date_updated', sa.DateTime(timezone=True),
                  nullable=False, index=True,
                  server_default=sa.func.current_timestamp())
    )
    op.create_table(
        'order_product',
        sa.Column('order_id', sa.Integer(), primary_key=True),
        sa.Column('product_id', sa.Integer(), primary_key=True),
        sa.Column('product_quantity', sa.Integer(), nullable=False),
        sa.Column('product_price', sa.Float(), nullable=False)
    )
    op.create_table(
        'order_history',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('order_id', sa.Integer(), nullable=False, index=True),
        sa.Column('status', sa.String(64), nullable=False, index=True),
        sa.Column('operator_id', sa.Integer(), nullable=False, index=True),
        sa.Column('date_created', sa.DateTime(timezone=True),
                  nullable=False, index=True,
                  server_default=sa.func.current_timestamp())
    )
    op.create_table(
        'shopping_trolley',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), nullable=False, index=True),
        sa.Column('product_info', sa.PickleType(), nullable=True),
        sa.Column('date_created', sa.DateTime(timezone=True),
                  nullable=False, index=True,
                  server_default=sa.func.current_timestamp()),
        sa.Column('date_updated', sa.DateTime(timezone=True),
                  nullable=False, index=True,
                  server_default=sa.func.current_timestamp())
    )
    op.create_table(
        'pay',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('order_id', sa.Integer(), nullable=False, index=True),
        sa.Column('status', sa.String(64), nullable=False, index=True),
        sa.Column('date_created', sa.DateTime(timezone=True),
                  nullable=False, index=True,
                  server_default=sa.func.current_timestamp()),
        sa.Column('date_updated', sa.DateTime(timezone=True),
                  nullable=False, index=True,
                  server_default=sa.func.current_timestamp())
    )
    op.create_table(
        'product',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(64), nullable=False, index=True),
        sa.Column('category', sa.String(64), nullable=False),
        sa.Column('description', sa.UnicodeText(), nullable=True),
        sa.Column('price', sa.Float(), nullable=False, index=True),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('made_in', sa.String(64), nullable=False),
        sa.Column('date_created', sa.DateTime(timezone=True),
                  nullable=False, index=True,
                  server_default=sa.func.current_timestamp()),
        sa.Column('date_updated', sa.DateTime(timezone=True),
                  nullable=False, index=True,
                  server_default=sa.func.current_timestamp())
    )
    op.create_table(
        'lacked_product_history',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('product_id', sa.Integer(), nullable=False, index=True),
        sa.Column('order_id', sa.Integer(), nullable=False, index=True),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('date_created', sa.DateTime(timezone=True), nullable=False,
                  server_default=sa.func.current_timestamp())
    )
    op.create_table(
        'purchase',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('product_id', sa.Integer(), nullable=False, index=True),
        sa.Column('product_quantity', sa.Integer(), nullable=False),
        sa.Column('status', sa.String(64), nullable=False, index=True),
        sa.Column('date_created', sa.DateTime(timezone=True),
                  nullable=False, index=True,
                  server_default=sa.func.current_timestamp()),
        sa.Column('date_updated', sa.DateTime(timezone=True),
                  nullable=False, index=True,
                  server_default=sa.func.current_timestamp())
    )
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(64), nullable=False, index=True),
        sa.Column('avatar', sa.String(512), nullable=False),
        sa.Column('phone', sa.String(), nullable=True),
        sa.Column('address', sa.String(), nullable=True),
        sa.Column('credit', sa.String(), nullable=False, index=True),
        sa.Column('date_created', sa.DateTime(timezone=True), nullable=False,
                  server_default=sa.func.current_timestamp())
    )
    op.create_table(
        'admin',
        sa.Column('user_id', sa.Integer(), primary_key=True),
        sa.Column('department', sa.String(16), nullable=False)
    )


def downgrade():
    op.drop_table('auth')
    op.drop_table('order')
    op.drop_table('order_product')
    op.drop_table('order_history')
    op.drop_table('shopping_trolley')
    op.drop_table('pay')
    op.drop_table('product')
    op.drop_table('lacked_product_history')
    op.drop_table('purchase')
    op.drop_table('user')
    op.drop_table('admin')
