
import pytest


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
def test_email_accepts_valid_input(email_page, email):
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
def test_email_rejects_invalid_input(email_page, email):
    email_page.open()
    email_page.submit_email(email)
    email_page.result_should_not_be_visible()

