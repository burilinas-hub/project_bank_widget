def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты по формату XXXX XX** **** XXXX"""
    # Удаляем пробелы
    new_card_number = card_number.replace(" ", "")

    # Проверка длины
    if len(new_card_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр.")

    # Проверка на цифры
    if not new_card_number.isdigit():
        raise ValueError("Номер карты должен состоять только из цифр.")

    # Формируем маску
    return new_card_number[:4] + " " + new_card_number[4:6] + "**" + " " + "****" + " " + new_card_number[-4:]


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета по формату **XXXX"""
    new_account_number = account_number.replace(" ", "")

    # Проверка длины
    if len(new_account_number) != 20:
        raise ValueError("Номер счета должен содержать 20 цифр.")

    # Проверка на цифры
    if not new_account_number.isdigit():
        raise ValueError("Номер счета должен состоять только из цифр.")

    # Возвращаем маску со звездочками и последними 4 цифрами
    return f"**{new_account_number[-4:]}"
