from src.masks import get_mask_card_number
from typing import List
from datetime import datetime


def mask_account_card(info: str) -> str:
    """Функция — которая добавляет название карты и маскирует номер."""
    parts: List[str] = info.split()
    # Первые два элемента — название карты
    card_type: str = " ".join(parts[:-1])  # Всё, кроме последнего
    number_str: str = parts[-1]
    # Маскируем номер (предполагается, что номер — это число)
    masked_number: str = get_mask_card_number(int(number_str))
    return f"{card_type} {masked_number}"


def get_date(date_str: str) -> str:
    """Функция, которая возвращает строку с датой в формате 'ДД.ММ.ГГГГ'."""
    # Парсим строку в объект datetime
    dt: datetime = datetime.fromisoformat(date_str)
    # Форматируем в "День. Месяц. Год"
    return dt.strftime("%d.%m.%Y")
