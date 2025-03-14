def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция фильтрует данные по указанному параметру"""

    new_list = []
    for element in list_dict:
        if element["state"] == state:
            new_list.append(element)

    return new_list


def sort_by_date(list_dict: list, reverse: bool = True) -> list:
    """Функция сортирует список словарей на основе ключа date"""

    return sorted(list_dict, key=lambda x: ["date"], reverse=reverse)
