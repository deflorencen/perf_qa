from playwright.sync_api import expect

def test_prompt_box(app):
    page = app.alerts.prompt_box
    page.open()

    expect(page.prompt_button).to_be_visible()
    expect(page.prompt_button).to_have_text("Click")

    page.click_button_and_handle_prompt("Playwright")
    expect(page.result_text).to_have_text("Playwright")

    page.click_button_and_handle_prompt("")
    expect(page.result_text).to_have_text("You entered nothing")