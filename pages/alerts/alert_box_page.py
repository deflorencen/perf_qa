from playwright.sync_api import Page, expect
from data.urls import Urls
from pages.base_result_page import BaseResultPage


class AlertBoxPage(BaseResultPage):
    URL = Urls.Elements.Alerts.ALERT_BOX

    def __init__(self, page: Page):
        super().__init__(page)
        self.alert_button = page.locator(".a-button")

    def click_button_and_accept_alert(self, expected_message: str):
        def handle_dialog(dialog):
            assert  dialog.type == "alert"
            if dialog.message != expected_message:
                dialog.dismiss()

            dialog.accept()

        self.page.once("dialog", handle_dialog)
        self.alert_button.click()

