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


class Product(db.Model):
    __tablename__ = 'product'

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


class UserRole:
    __tablename__ = 'user_role'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{self.__tablename__}: {self.id}'


class User:
    __tablename__ = 'User'

    tg_id = Column(BigInteger, primary_key=True)
    phone_number = Column(BigInteger)
    age = Column(Integer)
    role = Column(Integer, ForeignKey('user_role.id'))

    def __str__(self):
        return self.role

    def __repr__(self):
        return f'{self.__tablename__}: {self.tg_id}'


class OrderHistory:
    __tablename__ = 'order_history'

    id = Column(Integer, primary_key=True)
    order_sum = Column(BigInteger)
    product_quantity = Column(Integer)
    payer = Column(BigInteger, ForeignKey('user.tg_id'))
    delivery = Column(Boolean)

    def __str__(self):
        return self.payer

    def __repr__(self):
        return f'{self.__tablename__}: {self.id}'


class OrderProducts:
    __tablename__ = 'order_products'

    id = Column(Integer)
    order_id = Column(Integer, ForeignKey('order_history.id'))
    product_id = Column(Integer, ForeignKey('product.Id'))

    def __str__(self):
        return self.id

    def __repr__(self):
        return f'{self.__tablename__}: {self.id}'
