import pytest

@pytest.fixture
def valid_email():
    return "donald@gmail.com"

@pytest.fixture
def valid_text():
    return "hello!"

@pytest.fixture
def valid_password():
    return "DonaldTrump123@gmail.com"