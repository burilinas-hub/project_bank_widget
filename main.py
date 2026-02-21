from src.masks import get_mask_account, get_mask_card_number


def main() -> None:
    """Основная выполняемая программа"""
    try:
        card_input = input("Введите свой номер карты: ")
        print("Маскированный номер карты:", get_mask_card_number(card_input))
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        account_input = input("Введите свой номер счета: ")
        print("Маскированный номер счета:", get_mask_account(account_input))
    except ValueError as e:
        print(f"Ошибка: {e}")


main()
