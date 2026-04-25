from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery, Message

from database.utils import db_get_cart_items
from keyboards.inline import cart_actions_kb

router = Router()


@router.message(F.text == 'Корзина 🛒')
async def handle_cart(message: Message):
    '''показать содержимое корзины - reply кнопка'''
    chat_id = message.chat.id
    await show_cart(chat_id=chat_id, send_fn=message.answer)


@router.callback_query(F.data == 'Корзина заказа')
async def open_cart(callback: CallbackQuery):
    '''показать содержимое корзины - inline кнопка'''
    chat_id = callback.from_user.id
    await show_cart(chat_id=chat_id, send_fn=callback.message.answer)
    await callback.answer()

async def show_cart(chat_id: int, send_fn):
    '''🍉🍉🍉🍉🍉🍉'''
    cart_items = db_get_cart_items(chat_id) # TODO: сделать нормально

    if not cart_items:
        await send_fn('Корзина пуста')
        return
    text = 'сождержимое вашей корзины 🛒 🍉🍉🍉\n'
    total = 0
    for item in cart_items:
        total =float(item['final_price']) + total
        text += f'{item["product_name"]} - {item["quantity"]} шт. - {total}₽'

    text += f'\nИтого: {total}₽'
    await send_fn(text, reply_markup=cart_actions_kb())