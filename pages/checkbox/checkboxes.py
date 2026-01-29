from playwright.sync_api import Page, expect
from data.urls import Urls
from pages.base_result_page import BaseResultPage
from typing import List


class MultipleCheckboxPage(BaseResultPage):
    URL = Urls.Elements.Checkbox.MULTIPLE_CHECKBOX

    def __init__(self, page: Page):
        super().__init__(page)
        self.checkboxes = page.locator("input[type='checkbox']")
        self.submit_button = page.locator("#submit-id-submit")

    def click_submit(self):
        self.submit_button.click()

    def select_checkboxes_by_indices(self, indices: List[int]):
        for index in indices:
            self.checkboxes.nth(index).check()

    def result_should_math_selected(self, expected_text: str):
        self.result_should_be(expected_text)

    def submit_should_be_enabled(self):
        expect(self.submit_button).to_be_enabled()

    def checkboxes_count_should_be(self, count: int):
        all_checkboxes = self.page.locator("input[type='checkbox']")
        expect(all_checkboxes).to_have_count(count)
