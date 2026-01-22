
from playwright.sync_api import Page
from pages.buttons.looks_like_button_page import LikeAButtonPage
from pages.inputs.email_input_page import EmailInputPage
from pages.inputs.pass_input_page import PasswordInputPage
from pages.inputs.simple_input_page import InputPage
from pages.buttons.simple_button_page import SimpleButtonPage
from pages.buttons.disable_button_page import DisableButtonPage


class Application:
    def __init__(self, page: Page):
        self.page = page

        self.simple_input_page = InputPage(page)
        self.email_input_page = EmailInputPage(page)
        self.password_input_page = PasswordInputPage(page)
        self.simple_button_page = SimpleButtonPage(page)
        self.like_a_button_page = LikeAButtonPage(page)
        self.disable_button_page = DisableButtonPage(page)