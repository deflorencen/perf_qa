from playwright.sync_api import Page, expect
from data.urls import Urls
from pages.base_result_page import BaseResultPage


class ConfirmationAlertPage(BaseResultPage):
    URL = Urls.Elements.Alerts.CONFIRM_BOX

    def __init__(self, page: Page):
        super().__init__(page)
        self.confirmation_button = page.locator(".a-button")

    def click_alert_button_and_handle_confirmation(self, accept: bool = True):
        def handle_dialog(dialog):
            assert dialog.type == "confirm"
            dialog.accept() if accept else dialog.dismiss()
        self.page.once("dialog", handle_dialog)
        self.confirmation_button.click()
