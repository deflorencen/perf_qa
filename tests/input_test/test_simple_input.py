
import pytest
from playwright.sync_api import Page
from pages.inputs.simple_input_page import InputPage

#POSITIVE TEST
@pytest.mark.parametrize(
    "text",
    [
        "ab",                   # min length
        "hello_123",            # valid
        "a" * 25,               # max length
        "test-user_01",         # hyphen + underscore
    ]
)
def test_input_accepts_valid_text(page: Page, text):
    input_page = InputPage(page)

    input_page.open()
    input_page.submit_text(text)

    input_page.result_should_be(text)


#NEGATIVE TEST
@pytest.mark.parametrize(
    "text",
    [
        "",             # required
        "a",            # too short
        "a" * 26,       # too long
        "hello!!!",     # invalid chars
        "привет",       # cyrillic
    ]
)
def test_input_rejects_invalid_text(page: Page, text):
    input_page = InputPage(page)

    input_page.open()
    input_page.submit_text(text)

    input_page.result_should_not_be_visible()







