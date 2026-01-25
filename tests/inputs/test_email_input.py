import pytest
from data.test_data import EmailData


# POSITIVE TEST
@pytest.mark.parametrize("email", EmailData.VALID_EMAILS)
def test_email_accepts_valid_input(app, email):
    app.inputs.email_input_page.open()
    app.inputs.email_input_page.submit_email(email)
    app.inputs.email_input_page.result_should_be(email)


# NEGATIVE TEST
@pytest.mark.parametrize("email", EmailData.INVALID_EMAILS)
def test_email_rejects_invalid_input(app, email):
    app.inputs.email_input_page.open()
    app.inputs.email_input_page.submit_email(email)
    app.inputs.email_input_page.result_should_not_be_visible()

