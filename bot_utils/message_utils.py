def text_for_caption(name, description, base_price):
    """текст для описания товара"""
    text=(
        f"<b>{name}</b>\n"
        f"<b>Описание:</b> {description}\n"
        f"Цена: {base_price:.2F}/шт"

    )
    return text