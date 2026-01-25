from data.text_constants import ResultStates


def test_disabled_button_cannot_be_clicked(app):
    app.buttons.disable_button_page.open()
    app.buttons.disable_button_page.button_should_be_disabled()
    app.buttons.disable_button_page.select_state(ResultStates.ENABLED)
    app.buttons.disable_button_page.button_should_be_enabled()
    app.buttons.disable_button_page.select_state(ResultStates.DISABLED)
    app.buttons.disable_button_page.button_should_be_disabled()
    app.buttons.disable_button_page.select_state(ResultStates.ENABLED)
    app.buttons.disable_button_page.click_button()
    app.buttons.disable_button_page.result_should_be(ResultStates.SUBMITTED)