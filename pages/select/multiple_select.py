from playwright.sync_api import Page
from pages.base_result_page import BaseResultPage
from data.urls import Urls


class MultipleSelectPage(BaseResultPage):
    URL = Urls.Elements.Selectors.MULTIPLE_SELECT

    def __init__(self, page: Page):
        super().__init__(page)

        self.dropdown_place= page.locator("#id_choose_the_place_you_want_to_go")
        self.dropdown_transport = page.locator("#id_choose_how_you_want_to_get_there")
        self.dropdown_when = page.locator("#id_choose_when_you_want_to_go")

        self.label_place = page.locator("label[for='id_choose_the_place_you_want_to_go']")
        self.label_transport = page.locator("label[for='id_choose_how_you_want_to_get_there']")
        self.label_when = page.locator("label[for='id_choose_when_you_want_to_go']")

        self.submit_button = page.locator("#submit-id-submit")

    def click_submit(self):
        self.submit_button.click()

    def fill_form(self, place: str = None, transport: str = None, when: str = None):
        if place:
            self.dropdown_place.select_option(label=place)
        if transport:
            self.dropdown_transport.select_option(label=transport)
        if when:
            self.dropdown_when.select_option(label=when)