import sqlalchemy as sq
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
DSN = 'postgresql://postgres:46esehir@localhost:5432/homework'
engine = sq.create_engine(DSN)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    publisher_name = sq.Column(sq.String(length=40), unique=True)

    def __str__(self) -> str:
        return f"publisher {self.id}: {self.publisher_name}"


class Book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    book_title = sq.Column(sq.String(length=40))
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)
    publisher = relationship(Publisher, backref="book")
    def __str__(self) -> str:
        return f"book {self.id}: ({self.book_title}, {self.id_publisher})"


class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    shop_name = sq.Column(sq.String(length=40), nullable=False)
    
    def __str__(self) -> str:
        return f"shop {self.id}: {self.shop_name}"



class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    stock_count = sq.Column(sq.Integer)
    book = relationship(Book, backref='stock')
    shop = relationship(Shop, backref="stock")

    def __str__(self) -> str:
        return f"stock {self.id}: ({self.id_book}, {self.id_shop}, {self.stock_count})"
    


class Sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key=True)
    sale_price = sq.Column(sq.Numeric, nullable=False)
    date_sale = sq.Column(sq.DateTime, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
    sale_count = sq.Column(sq.Integer, nullable=False)
    stock = relationship(Stock, backref="sale")
    
    def __str__(self) -> str:
        return f"sale {self.id}: ({self.sale_price}, {self.date_sale}, {self.id_stock}, {self.sale_count})"
    
def create_tables(engine):
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

create_tables(engine)
session.commit()
session.close()