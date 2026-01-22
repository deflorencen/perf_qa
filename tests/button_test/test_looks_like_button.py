

def test_like_a_button_click(like_a_button_page):
    like_a_button_page.open()
    like_a_button_page.like_a_button_should_have_text("Click")
    like_a_button_page.click_like_a_button()
    like_a_button_page.result_should_be("Submitted")