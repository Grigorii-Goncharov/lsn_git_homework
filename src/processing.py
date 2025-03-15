def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрует данные по указанному параметру"""

    new_list = []
    for element in list_dict:
        if element["state"] == state:
            new_list.append(element)
    return new_list


def sort_by_date(list_dict: list[dict], value_sort: bool = True) -> list[dict]:
    """Функция сортирует список словарей о дате"""

    sort_list = sorted(list_dict, key=lambda x: x["date"], reverse=not value_sort)
    return sort_list
