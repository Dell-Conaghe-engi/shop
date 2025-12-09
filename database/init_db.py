import os
from itertools import product

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from database.base import Base
from database.models import Users, Carts, FinallyCarts, Categories, Products, Orders
from dotenv import load_dotenv


load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def init_db():
    print('создаём таблицы')
    Base.metadata.create_all(engine)
    print('таблицы gotovu')

    with SessionLocal() as session:

        categories = ["Торты", "Сыр", "Печенье"]
        category_map = {}

        for name in categories:
            category = session.scalar(select(Categories).filter_by(category_name=name))
            if not category:
                category = Categories(category_name=name)
                session.add(category)
                session.flush()
            category_map[name] = category.id

        products=[
            ("Торты", "Медовик", 45, "мёд, мука, сахар, яйца, масло", "media/hone_cake.jpg"),
            ("Торты", "Наполеон", 45, "мука, масло, молоко, яйца, соль", "media/napoleon_cake.jpg"),
            ("Торты", "Красный бархат", 45, "мука, масло, кефир, яйца, соль", "media/red_velvet_cake.jpg"),
            ("Сыр", "Моцарелла", 45, "молоко, вода", "media/mozzarella_cheese.jpg"),
            ("Сыр", "Чеддер", 45, "молоко, соль", "media/cheddar_cheese.jpg"),
            ("Сыр", "Бри", 45, "молоко", "media/brie_cheese"),
            ("Печенье","Орео", 45, "сахар, мука, вода, масло,соль", "media/oreo.jpg"),
            ("Печенье","Кукис", 45, "мука, масло, яйцо, сахар, шоколад", "media/cookies.jpg"),
            ("Печенье","Имбирное печенье", 45, "мёд, имбирь, мука, корица, соль", "media/ginger_cookies")]
        for category_name, name, price, desc, image in products:
            product_exists = session.scalar(select(Products).filter_by(product_name=name))
            if not product_exists:
                product = Products(
                    category_id=category_map[category_name],
                    product_name=name,
                    price=price,
                    description=desc,
                    image=image
                )
                session.add(product)

        session.commit()
        print("Первичные данные категорий ")

    if __name__ == "__main__":
        init_db()
