import pytest


# Фикстура для генерации номера карты
@pytest.fixture()
def test_string() -> str:
    return "7000 7922 8960 6361"


# Фикстура для генерации номера счета
@pytest.fixture()
def test_account_string() -> str:
    return "73654108430135874305"


# Фикстура для генерации даты
@pytest.fixture
def test_data_string() -> str:
    return "2023-10-26T00:00:00"
