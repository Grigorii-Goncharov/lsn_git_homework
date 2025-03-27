def get_mask_card_number(num_cart: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    card_number = str(num_cart).replace(" ", "")
    if len(card_number) != 16:
        raise ValueError("Введите 16 значный номер карты!")
    if not card_number.isdigit():
        raise ValueError("Введите числовое значение карты!")
    string = str(card_number)
    masked_card = f"{string[:4]} {string[4:6]}** **** {string[-4:]}"

    return masked_card


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход н принимает на вход номер счета и возвращает его маску."""
    if len(str(account_number)) != 20:
        raise ValueError("Номер счета должен состоять из 20 цифр!")
    if not str(account_number).isdigit():
        raise ValueError("Введите числовое значение счета!")
    string = str(account_number)
    masked_account_number = f"**{string[-4:]}"

    return masked_account_number
