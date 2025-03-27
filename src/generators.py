from typing import Any, Generator, Iterator

def filter_by_currency(transactions: list[dict[str, Any]], currency: str = "USD") -> Iterator[dict[str, Any]]:
    """Функция перебора списка словарей, она принимает на вход список словарей и возвращает
    итератор который выдает транзакции если они соответствуют заданной валюте"""

    for transaction in transactions:
        if transaction ["operationAmount"]["currency"]["code"] == currency:
            yield transaction

new_list_usd_transactions: list[dict[str, Any]] = []
usd_transactions = iter(filter_by_currency(new_list_usd_transactions, "USD"))
for _ in range(2):
    try:
        print(next(usd_transactions))
    except StopIteration:
        print("Больше нет данных")
        break

def transaction_descriptions(transactions: list[dict[str, Any]]) -> Iterator[str]:
    """Функция для генератора списков, которая принимает на вход список словарей и возвращает описание каждой
    операции по очереди"""
    for transaction in transactions:
        description = transaction.get("description")
        if description is not None:
            yield description

transactions_two: list[dict[str, Any]] = []
descriptions = transaction_descriptions(transactions_two)

for _ in range(5):
    try:
        print(next(descriptions))
    except StopIteration:
        print("Больше нет данных")
        break