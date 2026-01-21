import pytest
from pages.inputs.email_input_page import EmailInputPage
from pages.inputs.pass_input_page import PasswordInputPage
from pages.inputs.simple_input_page import InputPage


@pytest.fixture
def email_page(page):
    return EmailInputPage(page)

@pytest.fixture
def password_page(page):
    return PasswordInputPage(page)

@pytest.fixture
def simple_input_page(page):
    return InputPage(page)