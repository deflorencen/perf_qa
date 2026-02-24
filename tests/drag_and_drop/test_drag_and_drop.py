from playwright.sync_api import expect


def test_drag_and_drop_box(app):
    page = app.interactions.boxes_page
    page.open()

    expect(page.drop_here_box).to_be_visible()
    expect(page.drop_here_box).to_have_text("Drop here")
    expect(page.drag_box).to_be_visible()
    expect(page.drag_box).to_have_text("Drag me")

    page.drag_and_drop()
    expect(page.drop_here_box).to_have_text("Dropped! Drag me")
