from playwright.sync_api import Page
from pages.base_result_page import BaseResultPage
from data.urls import Urls


class IframePopUpPage(BaseResultPage):
    URL = Urls.Elements.PopUps.IFRAME_POP_UP

    def __init__(self, page: Page):
        super().__init__(page)
        self.launch_button = page.get_by_role("button", name="Launch Pop-Up")

        self.modal = page.locator("#exampleModal")
        self.iframe = page.frame_locator("iframe")