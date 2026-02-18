from playwright.sync_api import expect

def test_new_tab_button_opens_in_new_tab(app):
    page = app.links.new_tab_button_page
    page.open()

    with page.page.expect_popup() as popup_info:
        page.click_button()

    new_tab = popup_info.value
    new_tab.wait_for_load_state()
    expect(new_tab).to_have_url("https://www.qa-practice.com/elements/new_tab/new_page")

    result_text = new_tab.locator("#result-text")
    expect(result_text).to_have_text("I am a new page in a new tab")
    expect(result_text).to_be_visible()

    new_tab.close()