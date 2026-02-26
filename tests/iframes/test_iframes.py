
from playwright.sync_api import expect

def test_iframes(app):
    page = app.iframe.simple_iframe_page
    page.open()
    page.iframe.locator(".navbar-toggler-icon").click()
