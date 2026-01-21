from playwright.sync_api import Page
from pages.base_result_page import BaseResultPage


class EmailInputPage(BaseResultPage):
    URL = "https://www.qa-practice.com/elements/input/email"

    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = page.get_by_placeholder("Submit me")


    def submit_email(self, email: str):
        self.email_input.fill(email)
        self.email_input.press("Enter")