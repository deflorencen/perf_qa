from data.text_constants import ResultStates


def test_button_click(app):
    app.buttons.simple_button_page.open()
    app.buttons.simple_button_page.button_should_have_text(ResultStates.CLICK)
    app.buttons.simple_button_page.click_button()
    app.buttons.simple_button_page.result_should_be(ResultStates.SUBMITTED)