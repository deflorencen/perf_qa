
import pytest
from playwright.sync_api import Page
from pages.inputs.pass_input_page import PasswordInputPage


# POSITIVE TEST
@pytest.mark.parametrize(
    "password",
    [
        "Abcdef1!",
        "StrongPass1$",
        "P@ssword123",
        "Qwerty9*",
        "Aa1!Aa1!"
    ]
)
def test_input_password(page: Page, password):
    password_page = PasswordInputPage(page)

    password_page.open()
    password_page.submit_password(password)

    password_page.result_should_be(password)


# NEGATIVE TEST
@pytest.mark.parametrize(
    "password",
    [
        "",
        "short1!",
        "alllowercase1!",
        "ALLUPPERCASE1!",
        "NoDigits!",
        "NoSpecial1",
        "12345678!",
        "abcdefgh",
    ]
)
def test_password_rejects_invalid_input(page: Page, password):
    password_page = PasswordInputPage(page)

    password_page.open()
    password_page.submit_password(password)

    password_page.result_should_not_be_visible()