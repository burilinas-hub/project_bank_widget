import pytest
from src.widjet import mask_account_card, get_date

@pytest.mark.parametrize(
    "info, expected_inclusions",
    [
        ("MasterCard 7000792289606361", ["MasterCard", "7000 79** **** 6361"]),
        # Можно добавить другие случаи, если есть
    ]
)
def test_mask_account_card(info, expected_inclusions):
    result = mask_account_card(info)
    for expected in expected_inclusions:
        assert expected in result

@pytest.mark.parametrize(
    "date_str, expected_date",
    [
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        # Можно добавить другие форматы или случаи
    ]
)
def test_get_date(date_str, expected_date):
    assert get_date(date_str) == expected_date

@pytest.mark.parametrize(
    "invalid_date",
    [
        "неформат даты",
        # Можно добавить другие некорректные строки
    ]
)
def test_get_date_invalid_format(invalid_date):
    with pytest.raises(ValueError):
        get_date(invalid_date)
