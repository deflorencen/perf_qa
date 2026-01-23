import pytest


# POSITIVE TEST
@pytest.mark.parametrize(
    "text",
    [
        "ab",                   # min length
        "hello_123",            # valid
        "a" * 25,               # max length
        "test-user_01",         # hyphen + underscore
    ]
)
def test_input_accepts_valid_text(app, text):
    app.inputs.simple_input_page.open()
    app.inputs.simple_input_page.submit_text(text)
    app.inputs.result_should_be(text)


# NEGATIVE TEST
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
def test_input_rejects_invalid_text(app, text):
    app.inputs.simple_input_page.open()
    app.inputs.simple_input_page.submit_text(text)
    app.inputs.simple_input_page.result_should_not_be_visible()







