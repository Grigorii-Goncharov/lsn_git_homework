import pytest


@pytest.fixture()
def test_string() -> str:
    return "7000 7922 8960 6361"


@pytest.fixture()
def test_account_string() -> str:
    return "73654108430135874305"
