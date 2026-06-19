def generate_cart_text(cart_items):
    '''генерация текста о содержимом корзины'''
    if not cart_items:
        return "Ваша корзина пуста"

    text = 'содержимое корзины:\n'
    total = 0.0

    for item in cart_items:
        name = item.get('product_name', 'неизвестный товар')
        quantity = item.get('quantity', 0)
        final_price = item.get('final_price', 0)

        total = float(final_price)
        text += f"{name}-{quantity} шт. - по {final_price}₽\n"
    text += f"Итого: {total}₽"
    return text