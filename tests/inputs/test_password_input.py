import pytest
from data.test_data import PasswordData


# POSITIVE TEST
@pytest.mark.parametrize("password", PasswordData.VALID_PASSWORDS)
def test_input_password(app, password):
    app.inputs.password_input_page.open()
    app.inputs.password_input_page.submit_password(password)
    app.inputs.password_input_page.result_should_be(password)


# NEGATIVE TEST
@pytest.mark.parametrize("password", PasswordData.INVALID_PASSWORDS)
def test_password_rejects_invalid_input(app, password):
    app.inputs.password_input_page.open()
    app.inputs.password_input_page.submit_password(password)
    app.inputs.password_input_page.result_should_not_be_visible()