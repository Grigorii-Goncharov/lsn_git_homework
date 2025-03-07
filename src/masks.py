def get_mask_card_number(num_cart: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    if len(str(num_cart)) != 16 or not str(num_cart).isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр!")

    string = str(num_cart)
    masked_card = f"{string[:4]} {string[4:6]}** **** {string[-4:]}"

    return masked_card


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход н принимает на вход номер счета и возвращает его маску."""
    if len(str(account_number)) != 20 or not str(account_number).isdigit():
        raise ValueError("Номер счета должен состоять из 20 цифр!")

    string = str(account_number)
    masked_account_number = f"**{string[-4:]}"

    return masked_account_number


card_exemple = 7000792289606341
account_exemple = 73654108430135874305

print(get_mask_card_number(card_exemple))
print(get_mask_account(account_exemple))
