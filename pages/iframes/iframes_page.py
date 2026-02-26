from playwright.sync_api import Page
from data.urls import Urls
from pages.base_result_page import BaseResultPage


class IframePage(BaseResultPage):
    URL = Urls.Elements.Iframes.IFRAME

    def __init__(self, page: Page):
        super().__init__(page)
        self.iframe = page.frame_locator("iframe")
        self.test_button = page.locator(".navbar-toggler-icon")