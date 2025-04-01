from typing import Any, List

import pytest


# Фикстура для генерации номера карты
@pytest.fixture()
def valid_string() -> str:
    return "7000792289606361"


# Фикстура для генерации номера счета
@pytest.fixture()
def valid_account_string() -> str:
    return "73654108430135874305"


# Фикстура для генерации даты
@pytest.fixture
def valid_data_string() -> str:
    return "2023-10-26T00:00:00"


# Фикстуры для генерации списка словарей
@pytest.fixture
def list_dict_info() -> List[Any]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_dict_info_same_date() -> List[Any]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T00:00:00"},
        {"id": 2, "state": "EXECUTED", "date": "2023-01-01T00:00:00"},
        {"id": 3, "state": "CANCELED", "date": "2023-01-01T00:00:00"},
    ]


@pytest.fixture
def list_dict_info_invalid_date() -> List[Any]:
    return [{"id": 1, "state": "EXECUTED", "date": "2023-01-01"}, {"id": 2, "state": "EXECUTED", "date": "01-02-2025"}]


@pytest.fixture
def list_dict_info_empty() -> List[Any]:
    return []


@pytest.fixture
def currency_basic() -> list[dict]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


@pytest.fixture
def currency_average() -> list[dict]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 123456789,
            "state": "EXECUTED",
            "date": "2023-05-15T14:22:10.123456",
            "operationAmount": {"amount": "15000.50", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Platinum 1234 5678 9012 3456",
            "to": "MasterCard 9876 5432 1098 7654",
        },
        {
            "id": 987654321,
            "state": "CANCELED",
            "date": "2022-11-30T09:45:33.789012",
            "operationAmount": {"amount": "500.00", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Оплата услуг",
            "from": "Счет 12345678901234567890",
            "to": "Счет 98765432109876543210",
        },
    ]
