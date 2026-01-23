

def test_like_a_button_click(app):
    app.buttons.like_a_button_page.open()
    app.buttons.like_a_button_page.like_a_button_should_have_text("Click")
    app.buttons.like_a_button_page.click_like_a_button()
    app.buttons.like_a_button_page.result_should_be("Submitted")