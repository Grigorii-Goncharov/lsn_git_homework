from typing import Any, Generator, Iterator


# def filter_by_currency(transactions: list[dict[str, Any]], currency: str = "USD") -> Iterator[dict[str, Any]]:
#     """Функция перебора списка словарей, она принимает на вход список словарей и возвращает
#     итератор который выдает транзакции если они соответствуют заданной валюте"""
#
#     for transaction in transactions:
#         if transaction["operationAmount"]["currency"]["code"] == currency:
#             yield transaction

def filter_by_currency(transactions, currency="USD"):
    currency = currency.upper()  # Нормализуем входную валюту
    for transaction in transactions:
        # JSON-формат
        if (
            "operationAmount" in transaction
            and isinstance(transaction["operationAmount"], dict)
            and "currency" in transaction["operationAmount"]
            and isinstance(transaction["operationAmount"]["currency"], dict)
            and str(transaction["operationAmount"]["currency"].get("code", "")).upper() == currency
        ):
            yield transaction
        # CSV/Excel-формат
        elif str(transaction.get("currency_code", "")).upper() == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict[str, Any]]) -> Iterator[str]:
    """Функция для генератора списков, которая принимает на вход список словарей и возвращает описание каждой
    операции по очереди"""
    for transaction in transactions:
        description = transaction.get("description")
        if description is not None:
            yield description


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Функция для генератора номеров банковских карт, который принимает на вход начальное и конечное значение
    карт в формате XXXX XXXX XXXX XXXX, где X— цифра номера карты и возвращает номера корт"""
    if start > stop:
        raise ValueError("Стартовое значение не может быть больше конечного")

    for i in range(start, stop + 1):
        # используется для заполнения строки нулями слева до достижения заданной ширины
        new_number_card = str(i).zfill(16)
        formatted_card = f"{new_number_card[:4]} {new_number_card[4:8]} {new_number_card[8:12]} {new_number_card[12:]}"
        yield formatted_card
