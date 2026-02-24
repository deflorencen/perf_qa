from playwright.sync_api import expect


def test_confirmation_alert(app):
    page = app.alerts.confirm_box
    page.open()

    expect(page.confirmation_button).to_be_visible()
    expect(page.confirmation_button).to_have_text("Click")

    page.click_alert_button_and_handle_confirmation(accept=True)
    expect(page.result_text).to_have_text("Ok")

    page.click_alert_button_and_handle_confirmation(accept=False)
    expect(page.result_text).to_have_text("Cancel")
