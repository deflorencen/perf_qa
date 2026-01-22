

def test_disabled_button_cannot_be_clicked(app):
    app.disable_button_page.open()
    app.disable_button_page.button_should_be_disabled()
    app.disable_button_page.select_state("Enabled")
    app.disable_button_page.button_should_be_enabled()
    app.disable_button_page.select_state("Disabled")
    app.disable_button_page.button_should_be_disabled()
    app.disable_button_page.select_state("Enabled")
    app.disable_button_page.click_button()
    app.disable_button_page.result_should_be("Submitted")