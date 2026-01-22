

def test_button_click(app):
    app.simple_button_page.open()
    app.simple_button_page.button_should_have_text("Click")
    app.simple_button_page.click_button()
    app.simple_button_page.result_should_be("Submitted")