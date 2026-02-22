def get_mask_card_number(card_number: int) -> str:
    """Маскирует номер карты по примеру:7000792289606361 -> 7000 79** **** 6361"""
    card_str = str(card_number)
    # Проверка длины
    if len(card_str) < 16:
        # Для коротких номеров можно просто скрыть всё
        return "*" * len(card_str)
    # Первые 4 цифры
    first_part = card_str[:4]
    # Последние 4 цифры
    last_part = card_str[-4:]
    # Остальные — заменяем звездочками по правилам
    middle_parts = [card_str[4:6] + "**", "****"]
    # Предполагаем, что формат: 4 цифры + 2 блока по 4 звездочки
    # Сделаем так, чтобы получилось, например:
    # "7000 79** **** 6361"
    # Для этого создадим соответствующие блоки
    # Первая часть после первых 4 цифр — 2 символа, звездочки
    # Вторая часть — оставшиеся блоки по 4 звездочки
    # Объединяем все части с пробелами
    masked_number = f"{first_part} {middle_parts[0]} {middle_parts[1]} {last_part}"
    return masked_number


def mask_account(account_number: str) -> str:
    """Маскирует номер счета, показывая только последние 4 цифры. Остальные заменяются на две звездочки."""
    account_str = str(account_number)
    if len(account_str) <= 4:
        return "*" * len(account_str)
    else:
        last4 = account_str[-4:]
        return f"Счет **{last4}"
