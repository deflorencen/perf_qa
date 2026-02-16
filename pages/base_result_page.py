from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class BaseResultPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.result_text = page.locator("#result-text")


    def result_should_be(self, expected_text: str):
        expect(self.result_text).to_be_visible()
        expect(self.result_text).to_have_text(expected_text)

    def result_should_not_be_visible(self):
        expect(self.result_text).not_to_be_visible()