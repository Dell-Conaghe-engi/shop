from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery
from config import MANAGER_ID
from database.utils import db_get_user_phone
from bot_utils.counting_products import counting_products

router = Router()


@router.callback_query(F.data == "confirm_order")
async def confirm_order(callback: CallbackQuery, bot: Bot):
    """Подтверждение заказа"""
    user = callback.from_user
    phone = db_get_user_phone(user.id)
    mention = f'<a href="tg://user?id={user.id}"> {user.full_name} </a>'
    user_text = f'новый заказ от {mention} с номером телефона: {phone}'
    context = counting_products(user.id, user_text)

    if not context:
        await callback.message.edit_text('корзина пуста')
        await callback.answer()
        return

    if not MANAGER_ID:
        await callback.message.edit_text('оформление заказа без товаров не возможно')
        await callback.answer()
        return
    count, text, total_price, cart_id = context
    await bot.send_message(MANAGER_ID, text, parse_mode='HTML')