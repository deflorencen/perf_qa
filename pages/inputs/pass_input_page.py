from playwright.sync_api import Page
from pages.base_page import BasePage

class PasswordInputPage(BasePage):
    URL = "https://www.qa-practice.com/elements/input/passwd"

    def __init__(self, page: Page):
        super().__init__(page)
        self.password_input = page.get_by_placeholder("Submit me")


    def submit_password(self, password: str):
        self.submit_and_enter(self.password_input, password)