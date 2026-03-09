import pytest
from src.masks import mask_account

# Фикстура с данными
@pytest.fixture
def account_test_data() -> list:
    return [
        ("Счет 1234567890", "Счет **7890"),
        ("1234", "****"),
    ]

def test_mask_account_with_fixture(account_test_data: list) -> None:
    for account_str, expected_output in account_test_data:
        assert mask_account(account_str) == expected_output

# Параметризация с разными наборами данных
@pytest.mark.parametrize(
    "account_str, expected_output",
    [
        ("Счет 1234567890", "Счет **7890"),
        ("1234", "****"),
    ]
)
def test_mask_account(account_str: str, expected_output: str, account_test_data: list) -> None:
    # Можно объединить данные из фикстуры и параметры, если нужно проверить оба варианта
    # Но проще оставить только параметры
    assert mask_account(account_str) == expected_output
