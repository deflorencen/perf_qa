import pytest

@pytest.fixture
def valid_email():
    return "donald@gmail.com"

@pytest.fixture
def valid_text():
    return "hello_123"

@pytest.fixture
def valid_password():
    return "DonaldTrump123@gmail.com"

@pytest.fixture
def min_length_text():
    return "ab"

@pytest.fixture
def max_length_text():
    return "a" * 25

@pytest.fixture
def too_short_text():
    return "a"

@pytest.fixture
def too_long_text():
    return "a" * 26

@pytest.fixture
def invalid_chars_text():
    return "hello!!!"

@pytest.fixture
def cyrillic_text():
    return "привет"
