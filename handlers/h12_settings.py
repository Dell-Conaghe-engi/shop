from aiogram import Router, F
from aiogram.types import CallbackQuery, Message

from keyboards.inline import get_settings_menu
from keyboards.reply import get_main_menu

router = Router()


@router.message(F.text == "Настройки ⚙️")
async def hendel_settings_menu(message: Message):
    '''обработка настроек'''
    await message.answer("Настройки 🍉", reply_markup=get_settings_menu())

@router.callback_query(F.data == "back_to_menu")
async def hendel_back_to_menu(callback: CallbackQuery):
    '''выход назад в меню из меню настроек'''
    await callback.message.delete()
    await callback.message.answer("Главное меню 🍉", reply_markup=get_main_menu())









