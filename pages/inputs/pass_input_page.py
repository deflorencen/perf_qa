from playwright.sync_api import Page
from pages.base_result_page import BaseResultPage


class PasswordInputPage(BaseResultPage):
    URL = "https://www.qa-practice.com/elements/input/passwd"

    def __init__(self, page: Page):
        super().__init__(page)
        self.password_input = page.get_by_placeholder("Submit me")


    def submit_password(self, password: str):
        self.password_input.fill(password)
        self.password_input.press("Enter")