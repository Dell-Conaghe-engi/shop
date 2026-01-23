from sqlalchemy.orm import Session
from database.base import engine
from database.models import Users, Carts, Categories, FinallyCarts
from sqlalchemy.exc import IntegrityError
from sqlalchemy import update, select, func, join

'''создание, чтение,изменение и удаление, данных с помощью функций в базу данных'''

def get_session():
    return Session(engine)


def db_register_user(full_name, chat_id):
    """ регистрация пользователя в базе данных """
    try:
        with get_session() as session:
            query = Users(name=full_name, telegram=chat_id)
            session.add(query)
            session.commit()
        return False
    except IntegrityError:
        return True


def db_update_user(chat_id, phone):
    '''обновление номера телефона пользователя в базе данных'''
    with get_session() as session:
        query = update(Users).where(Users.telegram == chat_id).values(phone=phone)
        session.execute(query)
        session.commit()


def db_create_user_cart(chat_id):
    '''создание корзины пользователя(одна корзина на одного пользователя)'''
    try:
        with get_session() as session:
            subquery = session.scalar(select(Users).where(Users.telegram == chat_id))
            query = Carts(user_id=subquery.id)
            session.add(query)
            session.commit()
            return True
    except IntegrityError:
        return False
    except AttributeError:
        return False

def db_get_all_categories():
    '''получение всех категорий из базы данных'''
    with get_session() as session:
        query = select(Categories)
        return session.scalars(query).all()

def db_get_finally_price(chat_id):
    """Получение итоговой цены"""

    with get_session() as session:
        query = select(func.sum(FinallyCarts.final_price)).select_from(
            join(Carts, FinallyCarts, Carts.id == FinallyCarts.cart_id)).join(Users, Users.id == Carts.user_id).where(
            Users.telegram == chat_id)
        return session.execute(query).fetchone()[0]
