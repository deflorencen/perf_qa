from playwright.sync_api import Page, expect
from data.urls import Urls
from pages.base_result_page import BaseResultPage

class LikeAButtonPage(BaseResultPage):
    URL = Urls.LIKE_A_BUTTON

    def __init__(self, page: Page):
        super().__init__(page)
        self.like_a_button = page.get_by_role("link", name="Click")

    def click_like_a_button(self):
        self.like_a_button.click()

    def like_a_button_should_have_text(self, expected_text: str):
        expect(self.like_a_button).to_have_text(expected_text)