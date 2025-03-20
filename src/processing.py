def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрует данные по указанному параметру 'state'"""

    new_list = []
    for item in list_dict:
        if item["state"] == state:
            new_list.append(item)
    return new_list


def sort_by_date(list_dict: list[dict], value_sort: bool = True) -> list[dict]:
    """Функция сортирует список словарей по дате"""

    sort_list = sorted(list_dict, key=lambda x: x["date"], reverse=value_sort)
    return sort_list
