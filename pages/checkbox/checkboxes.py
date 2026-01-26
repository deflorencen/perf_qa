from playwright.sync_api import Page
from data.urls import Urls
from pages.base_result_page import BaseResultPage


class MultipleCheckboxPage(BaseResultPage):
    URL = Urls.Elements.Checkbox.MULTIPLE_CHECKBOX

    def __init__(self, page: Page):
        super().__init__(page)
        self.checkbox1 = page.locator("#id_checkboxes_0")
        self.checkbox2 = page.locator("#id_checkboxes_1")
        self.checkbox3 = page.locator("#id_checkboxes_2")



