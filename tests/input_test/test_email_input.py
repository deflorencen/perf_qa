
from playwright.sync_api import Page
from pages.inputs.email_input_page import EmailInputPage

def test_input_email(page: Page, valid_email):
    email_page = EmailInputPage(page)

    email_page.open()
    email_page.submit_email(valid_email)

    email_page.result_should_be(valid_email)