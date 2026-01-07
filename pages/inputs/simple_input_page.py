from playwright.sync_api import Page
from pages.base_page import BasePage

class InputPage(BasePage):
    URL = "https://www.qa-practice.com/elements/input/simple"

    def __init__(self, page: Page):
        super().__init__(page)
        self.input_field = page.locator("#id_text_string")
        self.email_link = page.get_by_text("Email field")


    def submit_text(self, text: str):
        self.submit_and_enter(self.input_field, text)