from playwright.sync_api import Page, expect
from pages.base_result_page import BaseResultPage

class SimpleButtonPage(BaseResultPage):
    URL = "https://www.qa-practice.com/elements/button/simple"

    def __init__(self, page: Page):
        super().__init__(page)
        self.simple_button = page.get_by_role("button", name="Click")


    def click_button(self):
        self.simple_button.click()

    def button_should_have_text(self, expected_text: str):
        expect(self.simple_button).to_have_text(expected_text)