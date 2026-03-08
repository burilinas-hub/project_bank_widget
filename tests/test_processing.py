import pytest
from src.processing import filter_by_state, sort_by_date

# Исходные данные для тестов
data = [
    {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
]

@pytest.mark.parametrize(
    "state_value, expected_states, expected_len",
    [
        (None, ["EXECUTED"], 2),  # Фильтр по умолчанию (если None, фильтр по "EXECUTED")
        ("CANCELED", ["CANCELED"], 1),
    ]
)
def test_filter_by_state(state_value, expected_states, expected_len):
    # Передача None для дефолтного случая
    result = filter_by_state(data, state_value) if state_value else filter_by_state(data)
    assert all(item["state"] in expected_states for item in result)
    assert len(result) == expected_len


@pytest.mark.parametrize(
    "reverse_order, expected_dates_order",
    [
        (True, ["2019-07-03T18:35:29.512364", "2018-09-12T21:27:25.241689", "2018-06-30T02:08:58.425572"]),
        (False, ["2018-06-30T02:08:58.425572", "2018-09-12T21:27:25.241689", "2019-07-03T18:35:29.512364"]),
    ]
)
def test_sort_by_date(reverse_order, expected_dates_order):
    sorted_data = sort_by_date(data, reverse=reverse_order)
    dates = [item["date"] for item in sorted_data]
    assert dates == expected_dates_order
