
from playwright.sync_api import expect

def test_text_area_interface(app):
    page = app.textarea.simple_text_area_page
    page.open()
    expect(page.submit_button).to_be_visible()

    page.fill_textarea("Hello, this is a test for the text area component.")
    expect(page.textarea).to_have_value("Hello, this is a test for the text area component.")
    expect(page.textarea).to_be_visible()
    page.click_submit()
    expect(page.result_text).to_have_text("Hello, this is a test for the text area component.")

    expect(page.label).to_have_text("Text area*")
    expect(page.textarea).to_be_visible()
    expect(page.submit_button).to_be_visible()