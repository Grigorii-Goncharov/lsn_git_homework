from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_account_number: str) -> str:
    """Функция маскировки счета и номера карты."""

    string_split = card_account_number.split()

    # Проверяем, является ли последний элемент числом (номер карты или счета)
    if not string_split[-1].isdigit():
        raise ValueError("Некорректный формат: отсутствует номер карты или счета")

    # Определяем тип (карта или счет)
    if "Счет" in card_account_number:
        if len(string_split) != 2 or len(string_split[-1]) != 20:
            raise ValueError("Некорректный формат счета")
        account_number = string_split[-1]
        masked_number = get_mask_account(account_number)
        return f"Счет {masked_number}"
    else:
        # Обрабатываем карту
        if len(string_split) < 2 or len(string_split[-1]) != 16:
            raise ValueError("Некорректный формат карты")
        card_number = string_split[-1]
        masked_number = get_mask_card_number(card_number)
        card_name = " ".join(string_split[:-1])
        return f"{card_name} {masked_number}"


def get_date(date_string: str) -> str:
    """Функция вывода даты"""

    # Разделяем дату и время
    date_part = date_string.split("T")[0]

    # Разделяем дату на год, месяц и день
    year, month, day = date_part.split("-")

    # Проверяем, что год, месяц и день являются числами
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        raise ValueError("Некорректный формат даты")

    # Формируем строку с датой в нужном формате
    formatted_date = f"{day}.{month}.{year}"
    return formatted_date
