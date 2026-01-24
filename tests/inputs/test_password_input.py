
import pytest


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
def test_input_password(app, password):
    app.inputs.password_input_page.open()
    app.inputs.password_input_page.submit_password(password)
    app.inputs.password_input_page.result_should_be(password)


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
def test_password_rejects_invalid_input(app, password):
    app.inputs.password_input_page.open()
    app.inputs.password_input_page.submit_password(password)
    app.inputs.password_input_page.result_should_not_be_visible()