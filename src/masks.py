from typing import List


def get_mask_card_number(card_number: int) -> str:
    """Маскирует номер карты по примеру: 7000792289606361 -> 7000 79** **** 6361."""
    card_str: str = str(card_number)
    # Проверка длины номера
    if len(card_str) < 16:
        # Для коротких номеров — маскируем всё
        return "*" * len(card_str)

    # Первые 4 цифры
    first_part: str = card_str[:4]
    # Последние 4 цифры
    last_part: str = card_str[-4:]
    # Остальные — маскируем по правилам
    middle_parts: List[str] = [card_str[4:6] + "**", "****"]

    # Объединяем части в финальный формат
    masked_number: str = f"{first_part} {middle_parts[0]} {middle_parts[1]} {last_part}"
    return masked_number


def mask_account(account_number: str) -> str:
    """Маскирует номер счета, показывая только последние 4 цифры.
    Остальные символы заменяются на две звездочки."""
    account_str: str = str(account_number)
    if len(account_str) <= 4:
        return "*" * len(account_str)
    else:
        last4: str = account_str[-4:]
        return f"Счет **{last4}"
