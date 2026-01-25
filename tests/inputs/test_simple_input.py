import pytest
from data.test_data import SimpleInputData


# POSITIVE TEST
@pytest.mark.parametrize("text", SimpleInputData.VALID_TEXTS)
def test_input_accepts_valid_text(app, text):
    app.inputs.simple_input_page.open()
    app.inputs.simple_input_page.submit_text(text)
    app.inputs.simple_input_page.result_should_be(text)


# NEGATIVE TEST
@pytest.mark.parametrize("text", SimpleInputData.INVALID_TEXTS)
def test_input_rejects_invalid_text(app, text):
    app.inputs.simple_input_page.open()
    app.inputs.simple_input_page.submit_text(text)
    app.inputs.simple_input_page.result_should_not_be_visible()







