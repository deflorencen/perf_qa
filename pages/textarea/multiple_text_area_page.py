from playwright.sync_api import Page
from pages.base_result_page import BaseResultPage
from data.urls import Urls


class MultipleTextAreaPage(BaseResultPage):
    URL = Urls.Elements.TextArea.MULTIPLE_TEXT_AREA

    def __init__(self, page: Page):
        super().__init__(page)
        self.first_area = page.locator("#id_first_chapter")
        self.second_area = page.locator("#id_second_chapter")
        self.third_area = page.locator("#id_third_chapter")

        self.label_first = page.locator("label[for='id_first_chapter']")
        self.label_second = page.locator("label[for='id_second_chapter']")
        self.label_third = page.locator("label[for='id_third_chapter']")

        self.submit_button = page.locator("#submit-id-submit")

    def fill_form(self, first: str = None, second: str = None, third: str = None):
        if first:
            self.first_area.fill(first)
        if second:
            self.second_area.fill(second)
        if third:
            self.third_area.fill(third)

    def click_submit(self):
        self.submit_button.click()