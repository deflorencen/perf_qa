from playwright.sync_api import Page
from data.urls import Urls
from pages.base_result_page import BaseResultPage


class DragNDropImagesPage(BaseResultPage):
    URL = Urls.Elements.Interactions.IMAGES

    def __init__(self, page: Page):
        super().__init__(page)
        self.rect1 = page.locator("#rect-droppable1")
        self.rect2 = page.locator("#rect-droppable2")
        self.image_box = page.locator("#rect-droppable1 img")

        self.message_in_box1 = self.rect1.locator("p.text-droppable")
        self.message_in_box2 = self.rect2.locator("p.text-droppable")

        self.image_in_box1 = self.rect1.locator("img")
        self.image_in_box2 = self.rect2.locator("img")

    def handle_drag_and_drop(self):
        if self.image_in_box2.is_visible():
             self.image_box.drag_to(self.rect1)
        self.image_box.drag_to(self.rect2)
