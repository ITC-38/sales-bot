"""initial

Revision ID: edeb7fd619fd
Revises: 
Create Date: 2023-04-20 19:54:51.451152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'edeb7fd619fd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('news',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('photo_path', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('sales',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('active_status', sa.Boolean(), nullable=True),
    sa.Column('sale_percent', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('user_role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inner_category',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category'], ['category.Id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('products',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('price', sa.BigInteger(), nullable=True),
    sa.Column('photo_path', sa.String(length=150), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('in_stock', sa.Boolean(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category'], ['category.Id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('user',
    sa.Column('tg_id', sa.BigInteger(), nullable=False),
    sa.Column('phone_number', sa.BigInteger(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('role', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role'], ['user_role.id'], ),
    sa.PrimaryKeyConstraint('tg_id')
    )
    op.create_table('cart',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('owner', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['owner'], ['user.tg_id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('order_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_sum', sa.BigInteger(), nullable=True),
    sa.Column('product_quantity', sa.Integer(), nullable=True),
    sa.Column('payer', sa.BigInteger(), nullable=True),
    sa.Column('delivery', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['payer'], ['user.tg_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sale_products',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('sales_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.Id'], ),
    sa.ForeignKeyConstraint(['sales_id'], ['sales.Id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('cart_product',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('cart', sa.Integer(), nullable=True),
    sa.Column('product', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cart'], ['cart.Id'], ),
    sa.ForeignKeyConstraint(['product'], ['products.Id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('order_products',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order_history.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.Id'], )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_products')
    op.drop_table('cart_product')
    op.drop_table('sale_products')
    op.drop_table('order_history')
    op.drop_table('cart')
    op.drop_table('user')
    op.drop_table('products')
    op.drop_table('inner_category')
    op.drop_table('user_role')
    op.drop_table('sales')
    op.drop_table('news')
    op.drop_table('category')
    # ### end Alembic commands ###
