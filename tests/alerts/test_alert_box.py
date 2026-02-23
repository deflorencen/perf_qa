from playwright.sync_api import expect


def test_simple_alert_box(app):
    page = app.alerts.alert_box
    page.open()

    expect(page.alert_button).to_have_text("Click")
    page.click_button_and_accept_alert("I am an alert!")