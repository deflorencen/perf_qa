import pytest

from pages.buttons.looks_like_button_page import LikeAButtonPage
from pages.inputs.email_input_page import EmailInputPage
from pages.inputs.pass_input_page import PasswordInputPage
from pages.inputs.simple_input_page import InputPage
from pages.buttons.simple_button_page import SimpleButtonPage
from pages.buttons.disable_button_page import DisableButtonPage


@pytest.fixture(scope="function")
def email_page(page) -> EmailInputPage:
    return EmailInputPage(page)

@pytest.fixture(scope="function")
def password_page(page) -> PasswordInputPage:
    return PasswordInputPage(page)

@pytest.fixture(scope="function")
def simple_input_page(page) -> InputPage:
    return InputPage(page)

@pytest.fixture(scope="function")
def simple_button_page(page) -> SimpleButtonPage:
    return SimpleButtonPage(page)

@pytest.fixture(scope="function")
def like_a_button_page(page) -> LikeAButtonPage:
    return LikeAButtonPage(page)

@pytest.fixture(scope="function")
def disabled_button_page(page) -> DisableButtonPage:
    return DisableButtonPage(page)