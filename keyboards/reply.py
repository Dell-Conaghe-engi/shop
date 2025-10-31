from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup


def start_kb():
    '''приветственная кнопка'''
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text='зайти в магазин 🏪')]],
        resize_keyboard=True
    )