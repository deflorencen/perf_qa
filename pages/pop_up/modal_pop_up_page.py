from playwright.sync_api import Page
from pages.base_result_page import BaseResultPage
from data.urls import Urls


class ModalPopUpPage(BaseResultPage):
    URL = Urls.Elements.PopUps.MODAL_POP_UP

    def __init__(self, page: Page):
        super().__init__(page)
        self.launch_button = page.get_by_role("button", name="Launch Pop-Up")

        self.modal = page.locator("#exampleModal")

        self.modal_title = self.modal.locator(".modal-header")
        self.checkbox = self.modal.locator("#id_checkbox_0")
        self.checkbox_label = self.modal.locator("label[for='id_checkbox_0']")

        self.send_button = self.modal.get_by_text("Send")
        self.cancel_button = self.modal.get_by_text("Close")

