from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery

from database.utils import db_get_user_cart, db_get_product_by_name, db_add_or_update_item
from handlers.h05_navigation import return_to_back

router = Router()


@router.callback_query(F.data == "положить в корзину")
async def add_to_cart(callback: CallbackQuery, bot: Bot):
    '''добовление товара в корзину'''
    chat_id = callback.message.chat.id
    message = callback.message

    caption = message.caption
    if not caption:
        await bot.send_message(chat_id=chat_id, text="Товара нет в корзине")
        return

    product_name = caption.split("\n")[0]

    cart = db_get_user_cart(chat_id)
    if not cart:
        await bot.send_message(chat_id=chat_id, text="необходима авторизация")
        return

    product = db_get_product_by_name(product_name)

    result = db_add_or_update_item(
        cart_id=cart.id,
        product_id=product.id,
        product_name=product_name,
        product_price=product.price,
        increment= 0)

    try:
        await bot.delete_message(chat_id=chat_id, message_id=message.message_id+1)
    except:
        pass

    try:
        await bot.delete_message(chat_id=chat_id, message_id=message.message_id)
    except:
        pass

    if result['status'] == 'ok':
        await bot.send_message(chat_id=chat_id, text="Товар добавлен в корзину")
    else:
        await bot.send_message(chat_id=chat_id, text="ошибка добавления товара в корзину")
    await return_to_back(message, bot)





