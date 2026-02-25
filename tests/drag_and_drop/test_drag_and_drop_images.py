from time import sleep

from playwright.sync_api import expect

def test_drag_and_drop_images(app):
    page = app.interactions.images_page
    page.open()

    # BASIC CONF., START TEST
    expect(page.rect1).to_be_visible()
    expect(page.rect2).to_be_visible()
    expect(page.image_box).to_have_attribute("src", "/static/home/smile.png")

    # DRAG IMAGE DO RECT2
    page.handle_drag_and_drop()
    expect(page.image_in_box2).to_have_attribute("src", "/static/home/smile.png")
    page.image_in_box2.click()

    # DRAG IMAGE BACK TO RECT1
    page.handle_drag_and_drop()
    expect(page.image_in_box1).to_have_attribute("src", "/static/home/smile.png")
