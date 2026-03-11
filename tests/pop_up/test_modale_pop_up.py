from playwright.sync_api import expect


def test_modal_pop_up(app):
    page = app.pop_ups.modal_pop_up_page
    page.open()

    expect(page.launch_button).to_be_visible()
    expect(page.launch_button).to_have_text("Launch Pop-Up")

    page.launch_button.click()
    expect(page.modal).to_be_visible()

    expect(page.checkbox).to_be_visible()
    page.checkbox.check()
    expect(page.checkbox).to_be_checked()

    expect(page.cancel_button).to_be_visible()
    expect(page.send_button).to_be_visible()

    page.send_button.click()
    expect(page.result_text).to_have_text("select me or not")
