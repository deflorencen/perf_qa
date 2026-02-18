from playwright.sync_api import Page
from pages.base_result_page import BaseResultPage
from data.urls import Urls


class NewTabButtonPage(BaseResultPage):
    URL = Urls.Elements.Links.TAB_BUTTON

    def __init__(self, page: Page):
        super().__init__(page)
        self.button = page.locator("#new-page-button")

    def click_button(self):
        self.button.click()