from playwright.sync_api import Page
from pages.base_result_page import BaseResultPage
from data.urls import Urls


class NewTabLinkPage(BaseResultPage):
    URL = Urls.Elements.Links.TAB_LINK

    def __init__(self, page: Page):
        super().__init__(page)
        self.link = page.locator("#new-page-link")

    def click_link(self):
        self.link.click()