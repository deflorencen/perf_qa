from playwright.sync_api import Page
from pages.base_result_page import BaseResultPage
from data.urls import Urls


class SimpleTextAreaPage(BaseResultPage):
    URL = Urls.Elements.TextArea.SIMPLE_TEXT_AREA

    def __init__(self, page: Page):
        super().__init__(page)
        self.textarea = page.locator("#id_text_area")
        self.submit_button = page.locator("#submit-id-submit")
        self.label = page.locator("label[for='id_text_area']")

    def fill_textarea(self, text: str):
        self.textarea.fill(text)

    def click_submit(self):
        self.submit_button.click()