from playwright.sync_api import Page, expect
from data.urls import Urls
from pages.base_result_page import BaseResultPage


class PromptBoxPage(BaseResultPage):
    URL = Urls.Elements.Alerts.PROMPT_BOX

    def __init__(self, page: Page):
        super().__init__(page)
        self.prompt_button = page.locator(".a-button")

    def click_button_and_handle_prompt(self, input_text: str, accept: bool = True):
        def handle_dialog(dialog):
            assert dialog.type == "prompt"
            if dialog.message != "Please enter some text":
                dialog.dismiss()
            else:
                if accept:
                    dialog.accept(input_text)
                else:
                    dialog.dismiss()

        self.page.once("dialog", handle_dialog)
        self.prompt_button.click()