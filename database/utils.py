from sqlalchemy.orm import Session
from database.base import engine
from database.models import Users, Carts
from sqlalchemy.exc import IntegrityError
from sqlalchemy import update, select

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
            query= Carts(user_id=subquery.id)
            session.add(query)
            session.commit()
            return True
    except IntegrityError:
        return False
    except AttributeError:
        return False

