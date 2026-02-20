
from playwright.sync_api import expect


def test_multiple_text_area_interface(app):
    page = app.textarea.multiple_text_area_page
    page.open()
    expect(page.first_area).to_be_visible()
    expect(page.second_area).to_be_visible()
    expect(page.third_area).to_be_visible()
    expect(page.submit_button).to_be_visible()

    expect(page.first_area).to_have_attribute("required", "")
    page.fill_form(first="This is the first text area.")
    expect(page.first_area).to_have_value("This is the first text area.")
    page.fill_form(second="This is the second text area.")
    expect(page.second_area).to_have_value("This is the second text area.")
    page.fill_form(third="This is the third text area.")
    expect(page.third_area).to_have_value("This is the third text area.")

    page.click_submit()
    expect(page.result_text).to_have_text("This is the first text area.This is the second text area.This is the third text area.")
    expect(page.result_text).to_be_visible()