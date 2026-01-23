from playwright.sync_api import Page
from pages.base_result_page import BaseResultPage
from data.urls import Urls


class InputPage(BaseResultPage):
    URL = Urls.SIMPLE_INPUT

    def __init__(self, page: Page):
        super().__init__(page)
        self.input_field = page.locator("#id_text_string")


    def submit_text(self, text: str):
        self.input_field.fill(text)
        self.input_field.press("Enter")