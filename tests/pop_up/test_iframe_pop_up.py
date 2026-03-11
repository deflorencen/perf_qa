from playwright.sync_api import expect


def test_iframe_pop_up(app):
    page = app.pop_ups.iframe_pop_up_page
    page.open()

    expect(page.launch_button).to_be_visible()
    expect(page.launch_button).to_have_text("Launch Pop-Up")

    page.launch_button.click()