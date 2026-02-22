from src.masks import get_mask_card_number
from datetime import datetime


def mask_account_card(info: str) -> str:
    """Функция - которая добавляет название карты и маскирует номер"""
    parts = info.split()
    # Первые два элемента — название карты
    card_type = " ".join(parts[:-1])  # всё, кроме последнего, например "Visa Platinum"
    number_str = parts[-1]
    # Маскируем номер
    masked_number = get_mask_card_number(int(number_str))
    return f"{card_type} {masked_number}"


def get_date(date_str: str) -> str:
    """Функция, которая возвращает строку с датой в формате "ДД.ММ.ГГГГ"""
    # Парсим строку в объект datetime
    dt = datetime.fromisoformat(date_str)
    # Форматируем в "День. Месяц. Год"
    return dt.strftime("%d.%m.%Y")