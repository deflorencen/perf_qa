
import pytest
from playwright.sync_api import Page
from pages.inputs.email_input_page import EmailInputPage


# POSITIVE TEST
@pytest.mark.parametrize(
    "email",
    [
        "test@example.com",
        "user.name@test-domain.com",
        "user_name123@test.co.uk",
        "a@b.io",
        "test@localhost",          # localhost allowed
    ]
)
def test_email_accepts_valid_input(page: Page, email):
    email_page = EmailInputPage(page)

    email_page.open()
    email_page.submit_email(email)

    email_page.result_should_be(email)

# NEGATIVE TEST
@pytest.mark.parametrize(
    "email",
    [
        "",                     # required
        "plainaddress",         # no @
        "@example.com",         # no local part
        "user@",                # no domain
        "user@.com",            # invalid domain
        "user@domain",          # no TLD (except localhost!)
        "user@domain..com",     # double dot
        "user domain@test.com", # space
        "user@домен.com",       # cyrillic
    ]
)
def test_email_rejects_invalid_input(page: Page, email):
    email_page = EmailInputPage(page)

    email_page.open()
    email_page.submit_email(email)

    email_page.result_should_not_be_visible()

