import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]


@pytest.mark.parametrize("currency_code,expected_ids", [
    ("USD", [939719570, 142264268, 895315941]),
    ("RUB", [873106923, 594226727]),
    ("EUR", [])  # Нет транзакций в EUR
])
def test_filter_by_currency(sample_transactions, currency_code, expected_ids):
    result = list(filter_by_currency(sample_transactions, currency_code))
    result_ids = [t['id'] for t in result]
    assert result_ids == expected_ids


@pytest.mark.parametrize("expected_descriptions", [
    [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ],
])
def test_transaction_descriptions(sample_transactions, expected_descriptions):
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == expected_descriptions


def test_filter_by_currency_empty():
    data = []
    assert list(filter_by_currency(data, "USD")) == []


def test_transaction_descriptions_empty():
    assert list(transaction_descriptions([])) == []


@pytest.mark.parametrize(
    "start, end, expected_numbers",
    [
        (
            1, 1,
            ["0000 0000 0000 0001"]
        ),
        (
            1, 3,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003"
            ]
        ),
        (
             9999999999999990, 9999999999999992,
            [
                "9999 9999 9999 9990",
                "9999 9999 9999 9991",
                "9999 9999 9999 9992"
            ]
        ),
        (
            123456789012345, 123456789012347,
            [
                "0123 4567 8901 2345",
                "0123 4567 8901 2346",
                "0123 4567 8901 2347"
            ]
        ),
    ])
def test_card_number_generator(start, end, expected_numbers):
    gen = card_number_generator(start, end)
    result = list(gen)
    assert result == expected_numbers
    for number in result:
        parts = number.split()
        assert len(parts) == 4
        for part in parts:
            assert len(part) == 4
            assert part.isdigit()
