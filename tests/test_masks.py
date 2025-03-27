import pytest

from src.masks import get_mask_account, get_mask_card_number


# Параметризация различных вариантов маскировки номера карты
@pytest.mark.parametrize(
    "valid_string, expected",
    [
        ("7000 7922 8960 6361", "7000 79** **** 6361"),
        ("1596 8378 6870 5199", "1596 83** **** 5199"),
        ("6831 9824 7673 7658", "6831 98** **** 7658"),
    ],
)
def test_mask_card_number(valid_string: str, expected: str) -> None:
    assert get_mask_card_number(valid_string) == expected


# тестирование ввода номера карты короче 16 символов
def test_invalid_short_string(valid_string: str) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(valid_string[:-1])


# тестирование ввода номера карты больше 16 символов
def test_invalid_long_string(valid_string: str) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(valid_string + "1")


# тестирование ввода номера карты пустая строка
def test_invalid_empty_string() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("")


# Параметризация различных вариантов маскировки счёта
@pytest.mark.parametrize(
    "valid_account_string, expected",
    [
        ("73654108430135874305", "**4305"),
        ("67456108430135877703", "**7703"),
        ("86868686430135899999", "**9999"),
    ],
)
def test_mask_account_number(valid_account_string: str, expected: str) -> None:
    assert get_mask_account(valid_account_string) == expected


# тестирование ввода номера счёта короче 20 символов
def test_invalid_short_account_number(valid_account_string: str) -> None:
    with pytest.raises(ValueError):
        get_mask_account(valid_account_string[:-1])


# тестирование ввода номера счёта больше 20 символов
def test_invalid_long_account_number(valid_account_string: str) -> None:
    with pytest.raises(ValueError):
        get_mask_account(valid_account_string + "1")


# тестирование ввода номера счёта пустая строка
def test_invalid_empty_account_number() -> None:
    with pytest.raises(ValueError):
        get_mask_account("")
