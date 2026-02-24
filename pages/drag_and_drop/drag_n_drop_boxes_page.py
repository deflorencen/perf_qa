from playwright.sync_api import Page, expect
from data.urls import Urls
from pages.base_result_page import BaseResultPage


class DragNDropBoxesPage(BaseResultPage):
    URL = Urls.Elements.Interactions.BOXES

    def __init__(self, page: Page):
        super().__init__(page)
        self.drop_here_box = page.locator("#rect-droppable")
        self.drag_box = page.locator("#rect-draggable")

    def drag_and_drop(self):
        self.drag_box.drag_to(self.drop_here_box)