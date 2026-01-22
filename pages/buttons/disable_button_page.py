from playwright.sync_api import Page, expect
from pages.base_result_page import BaseResultPage

class DisableButtonPage(BaseResultPage):
    URL = "https://www.qa-practice.com/elements/button/disabled"

    def __init__(self, page: Page):
        super().__init__(page)
        self.submit_button = page.get_by_role("button", name="Submit")
        self.state_dropdown = page.locator("#id_select_state")


    def select_state(self, state_text: str):
        self.state_dropdown.select_option(label=state_text)

    def click_button(self):
        self.submit_button.click()

    def button_should_be_disabled(self):
        expect(self.submit_button).to_be_disabled()

    def button_should_be_enabled(self):
        expect(self.submit_button).to_be_enabled()