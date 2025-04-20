from datetime import datetime
from typing import Any


def filter_by_state(list_dict: list[Any], state: str = "EXECUTED") -> list[Any]:
    """Функция фильтрует данные по указанному параметру 'state'"""

    if not list_dict:
        raise ValueError("Элемент списка не является словарем")
    new_list = []

    for item in list_dict:
        if item.get("state") == state:
            new_list.append(item)
        elif item.get("state") == "":
            raise ValueError("Нет текста")
    return new_list


def sort_by_date(list_dict: list[Any], value_sort: bool = True) -> list[Any]:
    """Функция сортирует список словарей по дате"""
    for item in list_dict:
        try:
            datetime.fromisoformat(item["date"])
        except ValueError:
            raise ValueError(f"Некорректный формат даты: {item['date']}")

    sort_list = sorted(list_dict, key=lambda x: x["date"], reverse=value_sort)
    return sort_list
