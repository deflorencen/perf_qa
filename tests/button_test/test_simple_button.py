

def test_button_click(simple_button_page):
    simple_button_page.open()
    simple_button_page.button_should_have_text("Click")
    simple_button_page.click_button()
    simple_button_page.result_should_be("Submitted")