import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

from models import create_tables, Shop, Sale, Stock, Publisher, Book
Base = declarative_base()
DSN = 'postgresql://postgres:46esehir@localhost:5432/homework'
engine = sq.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

def search_publisher_name():
    q = session.query(Publisher).join(Book). join(Shop).join(Sale)
    input_pub_name = input('Введите имя издателя: ') 
    q_result = q.filter(Publisher.publisher_name == input_pub_name)
    for i in q_result.all():
        print(f"издатель: {input_pub_name} найден в магазине {q_result.name} c ID {q_result.id}")

if __name__ == 'main':
    search_publisher_name()


session.close()