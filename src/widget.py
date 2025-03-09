import masks


def mask_account_card(card_account_number: str) -> str:
    """Функция маскировки счета и номера карты."""

    string_split = card_account_number.split()

    # Проверяем, является ли последний элемент числом (номер карты или счета)
    if not string_split[-1].isdigit():
        return "Некорректный формат: отсутствует номер карты или счета"

    # Определяем тип (карта или счет)
    if "Счет" in card_account_number:
        if len(string_split) != 2 or len(string_split[-1]) != 20:
            return "Некорректный формат счета"
        account_number = string_split[-1]
        masked_number = masks.get_mask_account(account_number)
        return f"Счет {masked_number}"
    else:
        # Обрабатываем карту
        if len(string_split) < 2 or len(string_split[-1]) != 16:
            return "Некорректный формат карты"
        card_number = string_split[-1]
        masked_number = masks.get_mask_card_number(card_number)
        card_name = " ".join(string_split[:-1])
        return f"{card_name} {masked_number}"


def get_date(date_string: str) -> str:
    """Функция вывода даты"""
    try:
        # Разделяем дату и время
        date_part = date_string.split("T")[0]

        # Разделяем дату на год, месяц и день
        year, month, day = date_part.split("-")

        # Проверяем, что год, месяц и день являются числами
        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            return "Некорректный формат даты"

        # Формируем строку с датой в нужном формате
        formatted_date = f"{day}.{month}.{year}"
        return formatted_date
    except (IndexError, ValueError):
        return "Некорректный формат даты"

card_exemple = "Visa Platinum 7000792289606361"
card_exemple2 = "Счет 64686473678894779589"
date = "2024-03-11T02:26:18.671407"

print(mask_account_card(card_exemple))
print(mask_account_card(card_exemple2))
print(get_date(date))