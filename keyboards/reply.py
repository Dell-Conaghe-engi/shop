from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup

'''модуль для функций создающих кнопки под клавиатурой'''


def start_kb():
    '''приветственная кнопка'''
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text='зайти в магазин 🏪')]],
        resize_keyboard=True
    )


def phone_kb():
    '''кнопка для ввода телефона'''
    builder = ReplyKeyboardBuilder()
    builder.button(text='Отправьте ваш номер телефона', request_contact=True)
    return builder.as_markup(resize_keyboard=True)


def get_main_menu():
    '''формирование кнопок для меню'''
    builder = ReplyKeyboardBuilder()
    builder.button(text='Оформить заказ ✅')
    builder.button(text='История 📃')
    builder.button(text='Корзина 🛒')
    builder.button(text='Настройки ⚙️')
    builder.adjust(2, 2)
    return builder.as_markup(resize_keyboard=True)


def bake_to_main_menu():
    '''кнопка для возврата в главное меню'''
    builder = ReplyKeyboardBuilder()
    builder.button(text='Вернуться в главное меню 🏠')
    return builder.as_markup(resize_keyboard=True)