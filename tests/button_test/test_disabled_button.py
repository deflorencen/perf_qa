

def test_disabled_button_cannot_be_clicked(disabled_button_page):
    disabled_button_page.open()
    disabled_button_page.button_should_be_disabled()
    disabled_button_page.select_state("Enabled")
    disabled_button_page.button_should_be_enabled()
    disabled_button_page.select_state("Disabled")
    disabled_button_page.button_should_be_disabled()
    disabled_button_page.select_state("Enabled")
    disabled_button_page.click_button()
    disabled_button_page.result_should_be("Submitted")