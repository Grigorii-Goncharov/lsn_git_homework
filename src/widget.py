from masks import get_mask_card_number


def mask_account_card(string: str) -> tuple[str, str]:
    """Функция маскировки счета и номера карты."""
    string_split = string.split()
    name_card = " ".join(string_split[:-1])
    number_card = string_split[-1]

    return name_card, number_card


def get_date(string: str) -> str:
    """Функция вывода даты"""

    return f"{string[8:10]}.{string[5:7]}.{string[0:4]}"


test = "Visa Platinum 8990922113665229"
name_card, number_card = mask_account_card(test)
masked_number = get_mask_card_number(number_card)
print(f"{name_card}: {masked_number}")

test = "2024-03-11T02:26:18.671407"
print(get_date(test))
