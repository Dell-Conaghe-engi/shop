from aiogram import Router, F, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile

from keyboards.inline import generate_category_menu
from keyboards.reply import bake_to_main_menu

router = Router()

@router.message(F.text == 'Оформить заказ ✅')
async def make_order(message: Message, bot: Bot):
    '''Оброботка кнопки Оформить заказ с дальнейшим переходом в котегории товаров'''
    chat_id = message.chat.id
    await bot.send_message(chat_id, 'формируем заказ...', reply_markup=bake_to_main_menu())
    await message.answer(text='выберите категорию', reply_markup=generate_category_menu(chat_id))
