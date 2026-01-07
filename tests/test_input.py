
from playwright.sync_api import Page, expect
from pages.inputs.simple_input_page import InputPage
from pages.inputs.email_input_page import EmailInputPage
from pages.inputs.pass_input_page import PasswordInputPage

def test_input_text(page: Page, valid_text):
    input_page = InputPage(page)

    input_page.open()
    input_page.submit_text(valid_text)

    input_page.result_should_be(valid_text)


def test_input_email(page: Page, valid_email):
    email_page = EmailInputPage(page)

    email_page.open()
    email_page.submit_email(valid_email)

    email_page.result_should_be(valid_email)


def test_input_password(page: Page, valid_password):
    password_page = PasswordInputPage(page)

    password_page.open()
    password_page.submit_password(valid_password)

    password_page.result_should_be(valid_password)






