from src.transaction_filter import filter_transactions # ,count_operations_by_category
# from typing import Any, List

import pytest

def test_exact_match(transactions):
    '''Тест на точное совпадение "Перевод организации"'''
    result = filter_transactions(transactions, r"Перевод организации")
    assert result == [transactions[0]]


def test_case_insensitive_match(transactions):
    '''Тест поиска, если строка в верхнем регистре'''
    result = filter_transactions(transactions, r"ПЕРЕВОД ОРГАНИЗАЦИИ")
    assert result == [transactions[0]]


def test_partial_match(transactions):
    '''Тест поиска по части строки'''
    result = filter_transactions(transactions, r"Перевод")
    assert result == [transactions[0]]


def test_no_match(transactions):
    '''Тест, когда строка не найдена'''
    result = filter_transactions(transactions, r"Несуществующий текст")
    assert result == []


def test_empty_search_string(transactions):
    '''Тест, должен вернуть все транзакции'''
    result = filter_transactions(transactions, "")
    assert result == transactions