from sqlalchemy.orm import Session
from database.base import engine
from database.models import Users
from sqlalchemy.exc import IntegrityError

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