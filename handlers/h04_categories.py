from aiogram import Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery

from keyboards.inline import show_product_by_category, generate_category_menu

router = Router()


@router.callback_query(F.data.regexp(r"^category_(\d+)$"))
async def show_product(callback: CallbackQuery):
    """показ всех продуктов выбранной категории"""
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    category_id = int(callback.data.split('_')[-1])

    try:
        await callback.bot.edit_message_text(
            text='выберите продукт',
            chat_id=chat_id,
            message_id=message_id,
            reply_markup=show_product_by_category(category_id)
        )
    except TelegramBadRequest:
        await callback.answer('не удалось открыть выбранную категорию')


@router.callback_query(F.data == 'return_to_category')
async def return_to_category(callback: CallbackQuery):
    """возврат к списку котегорий"""
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id

    await callback.bot.edit_message_text(
        text='выберите категорию⬇️',
        chat_id=chat_id,
        message_id=message_id,
        reply_markup=generate_category_menu(chat_id)
    )
