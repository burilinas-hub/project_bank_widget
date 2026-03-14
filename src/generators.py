def filter_by_currency(transactions, currency_code):
    """
    Итератор, возвращающий транзакции с указанным кодом валюты.
    :param transactions: Список словарей с транзакциями
    :param currency_code: строка, код валюты, например 'USD'
    """
    for transaction in transactions:
        if transaction.get('operationAmount', {}).get('currency', {}).get('code') == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    """
    Генератор, возвращающий описание каждой транзакции.
    """
    for transaction in transactions:
        yield transaction.get('description', 'Нет описания')


def card_number_generator(start, end):
    """
    Генератор, выдающий номера карт в формате XXXX XXXX XXXX XXXX
    в диапазоне от start до end включительно.
    """
    for number in range(start, end + 1):
        # Форматируем число как 16 цифр с ведущими нулями
        num_str = f"{number:016d}"
        # Разбиваем на 4 части
        parts = [num_str[i:i+4] for i in range(0, 16, 4)]
        yield " ".join(parts)