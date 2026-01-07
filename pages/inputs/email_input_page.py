from playwright.sync_api import Page
from pages.base_page import BasePage

class EmailInputPage(BasePage):
    URL = "https://www.qa-practice.com/elements/input/email"

    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = page.get_by_placeholder("Submit me")


    def submit_email(self, email: str):
        self.submit_and_enter(self.email_input, email)