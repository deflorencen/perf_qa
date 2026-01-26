from tabnanny import check

from playwright.sync_api import Page, expect
from data.urls import Urls
from pages.base_result_page import BaseResultPage


class SingleCheckboxPage(BaseResultPage):
    URL = Urls.Elements.Checkbox.SINGLE_CHECKBOX

    def __init__(self, page: Page):
        super().__init__(page)
        self.checkbox = page.locator("#id_checkbox_0")
        self.submit_button = page.locator("#submit-id-submit")
        self.checkbox_label = page.locator("label[for='id_checkbox_0']")

    def check_checkbox(self):
        self.checkbox.check()

    def uncheck_checkbox(self):
        self.checkbox.uncheck()

    def submit_checkbox(self):
        self.submit_button.click()

    def checkbox_should_be_present_once(self):
        all_checkboxes = self.page.locator("input[type='checkbox']")
        expect(all_checkboxes).to_have_count(1)

    def checkbox_should_have_label(self, expected_text: str):
        expect(self.checkbox_label).to_have_text(expected_text)

    def submit_should_be_enabled(self):
        expect(self.submit_button).to_be_enabled()

