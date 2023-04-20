from gino import Gino
from sqlalchemy import (
    Column, Integer, String,
    DateTime, ForeignKey, BigInteger,
    Boolean
)

db = Gino()


class News(db.Model):

    __tablename__ = 'news'

    Id = Column(Integer, primary_key=True)
    name = Column(String(100))
    title = Column(String)
    created_date = Column(DateTime)
    photo_path = Column(String(150))

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{self.__tablename__}: {self.Id}'


class Category(db.Model):

    __tablename__ = 'category'

    Id = Column(Integer, primary_key=True)
    name = Column(String(100))

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{self.__tablename__}: {self.Id}'


class InnerCategory(db.Model):

    __tablename__ = 'inner_category'

    Id = Column(Integer, primary_key=True)
    name = Column(String(100))
    category = Column(Integer, ForeignKey('category.Id'))

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{self.__tablename__}: {self.Id}'


class Products(db.Model):

    __tablename__ = 'products'

    Id = Column(Integer, primary_key=True)
    name = Column(String(128))
    price = Column(BigInteger)
    photo_path = Column(String(150))
    title = Column(String)
    in_stock = Column(Boolean, default=True)
    quantity = Column(Integer)
    category = Column(
        Integer,
        ForeignKey('category.Id')
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{self.__tablename__}: {self.Id}'

class sales(db.Model):
    __tablename__ = 'sales'
    Id = Column(Integer, primary_key=True)
    active_status = Column(Boolean)
    sale_percent = (Integer)

class sale_products(db.Model):
    __tablename__ = 'sale_products'
    Id = Column(Integer)
    sales_id = Column(Integer, ForeignKey('sales.Id'))
    product_id = Column(Integer, ForeignKey('sales.Id'))

class cart(db.Model):
    __tablename__ = 'cart'
    Id = Column(Integer, primary_key=True)
    name = Column(String(128))

class cartProduct(db.Model):
    __tablename__ = 'cartProduct'
    Id = Colum(Integer)
    cart = Colum(Integer, ForeignKey('cart.Id'))
    product = Colum(String, ForeignKey('products.Id'))



