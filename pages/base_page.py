from playwright.sync_api import Page, expect

class BasePage:
    URL: str | None = None

    def __init__(self, page: Page):
        self.page = page
        self.result_text = page.locator("#result-text")


    def open(self):
        if not self.URL:
            raise ValueError("URL is not defined for this page")
        self.page.goto(self.URL)


    def submit_and_enter(self, locator, value: str):
        locator.fill(value)
        locator.press('Enter')


    def result_should_be(self, text: str):
        expect(self.result_text).to_have_text(text)