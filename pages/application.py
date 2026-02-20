
from playwright.sync_api import Page
from pages.buttons.looks_like_button_page import LikeAButtonPage
from pages.inputs.email_input_page import EmailInputPage
from pages.inputs.pass_input_page import PasswordInputPage
from pages.inputs.simple_input_page import InputPage
from pages.buttons.simple_button_page import SimpleButtonPage
from pages.buttons.disabled_button_page import DisableButtonPage
from pages.checkbox.single_checkbox import SingleCheckboxPage
from pages.checkbox.checkboxes import MultipleCheckboxPage
from pages.select.single_select import SingleSelectPage
from pages.select.multiple_select import MultipleSelectPage
from pages.new_tab.new_tab_link_page import NewTabLinkPage
from pages.new_tab.new_tab_button_page import NewTabButtonPage
from pages.textarea.text_area_page import SimpleTextAreaPage
from pages.textarea.multiple_text_area_page import MultipleTextAreaPage


class Application:
    def __init__(self, page: Page):
        self.page = page

        self.inputs = InputsGroup(page)
        self.buttons = ButtonsGroup(page)
        self.checkboxes = CheckboxGroup(page)
        self.selectors = SelectorGroup(page)
        self.links = NewTabGroup(page)
        self.textarea = TextAreaGroup(page)


class InputsGroup:
    def __init__(self, page: Page):
        self.simple_input_page = InputPage(page)
        self.email_input_page = EmailInputPage(page)
        self.password_input_page = PasswordInputPage(page)


class ButtonsGroup:
    def __init__(self, page: Page):
        self.simple_button_page = SimpleButtonPage(page)
        self.like_a_button_page = LikeAButtonPage(page)
        self.disable_button_page = DisableButtonPage(page)


class CheckboxGroup:
    def __init__(self, page: Page):
        self.single_checkbox_page = SingleCheckboxPage(page)
        self.multiple_checkbox_page = MultipleCheckboxPage(page)


class SelectorGroup:
    def __init__(self, page: Page):
        self.single_select_page = SingleSelectPage(page)
        self.multiple_select_page = MultipleSelectPage(page)


class NewTabGroup:
    def __init__(self, page: Page):
        self.new_tab_link_page = NewTabLinkPage(page)
        self.new_tab_button_page = NewTabButtonPage(page)


class TextAreaGroup:
    def __init__(self, page: Page):
        self.simple_text_area_page = SimpleTextAreaPage(page)
        self.multiple_text_area_page = MultipleTextAreaPage(page)
