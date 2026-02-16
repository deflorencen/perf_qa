from playwright.sync_api import Page
from pages.base_result_page import BaseResultPage
from data.urls import Urls


class SingleSelectPage(BaseResultPage):
    URL = Urls.Elements.Selectors.SINGLE_SELECT

    def __init__(self, page: Page):
        super().__init__(page)
        self.select_dropdown = page.locator("#id_choose_language")
        self.submit_button = page.locator("#submit-id-submit")
        self.label = page.locator("label[for='id_choose_language']")

    def select_option(self, option_text: str):
        self.select_dropdown.select_option(label=option_text)

    def click_submit(self):
        self.submit_button.click()