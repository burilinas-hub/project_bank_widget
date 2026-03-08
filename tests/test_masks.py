import pytest
from src.masks import get_mask_card_number, mask_account

@pytest.mark.parametrize(
    "card_number, expected_output",
    [
        (7000792289606361, "7000 79** **** 6361"),
        (12345, "*****"),
    ]
)
def test_get_mask_card_number(card_number, expected_output):
    assert get_mask_card_number(card_number) == expected_output

@pytest.mark.parametrize(
    "account_str, expected_output",
    [
        ("Счет 1234567890", "Счет **7890"),
        ("1234", "****"),
    ]
)
def test_mask_account(account_str, expected_output):
    assert mask_account(account_str) == expected_output
