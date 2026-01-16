from aiogram.utils.keyboard import InlineKeyboardBuilder


def generate_category_menu(chat_id):
    '''создоние клавиатуры с выбором категорий'''
    categories = db_get_all_categories()
    total_price = db_get_finally_price(chat_id)

    builder = InlineKeyboardBuilder()
    builder.button(
        text=f"корзина заказа ({total_price if total_price else 0} руб.)",
        callback_data="Корзина заказа"
    )
    [builder.button(text=category.category_name, callback_data=f'category_{category.id}')
     for category in categories]
    builder.adjust(1,2)
    return builder.as_markup()