import pytest

from src.masks import get_mask_card_number, mask_account


# Аннотации типов для функции test_get_mask_card_number
@pytest.mark.parametrize(
    "card_number, expected_output",
    [
        (7000792289606361, "7000 79** **** 6361"),
        (12345, "*****"),
    ]
)
def test_get_mask_card_number(card_number: int, expected_output: str) -> None:
    assert get_mask_card_number(card_number) == expected_output


# Аннотации типов для функции test_mask_account
@pytest.mark.parametrize(
    "account_str, expected_output",
    [
        ("Счет 1234567890", "Счет **7890"),
        ("1234", "****"),
    ]
)
def test_mask_account(account_str: str, expected_output: str) -> None:
    assert mask_account(account_str) == expected_output
