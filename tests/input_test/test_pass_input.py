
from playwright.sync_api import Page
from pages.inputs.pass_input_page import PasswordInputPage


def test_input_password(page: Page, valid_password):
    password_page = PasswordInputPage(page)

    password_page.open()
    password_page.submit_password(valid_password)

    password_page.result_should_be(valid_password)