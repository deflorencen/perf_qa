import pytest
from playwright.sync_api import expect


def test_single_select_interface(app):
    page = app.selectors.single_select_page
    page.open()

    expect(page.label).to_have_text("Choose language*")
    expect(page.select_dropdown).to_have_attribute("required", "")


@pytest.mark.parametrize("language", ["Python", "Ruby", "JavaScript", "Java", "C#"])
def test_select_any_option(app, language):
    page = app.selectors.single_select_page
    page.open()
    page.select_option(language)
    page.click_submit()

    expect(page.result_text).to_have_text(language)