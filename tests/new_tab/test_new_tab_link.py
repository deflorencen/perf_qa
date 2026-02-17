import pytest
from playwright.sync_api import expect


def test_new_tab_link_opens_in_new_tab(app):
    page = app.links.new_tab_link_page
    page.open()

    with page.page.expect_popup() as popup_info:
        page.click_link()

    new_tab = popup_info.value
    new_tab.wait_for_load_state()
    expect(new_tab).to_have_url("https://www.qa-practice.com/elements/new_tab/new_page")

    result_text = new_tab.locator("#result-text")
    expect(result_text).to_have_text("I am a new page in a new tab")
    expect(result_text).to_be_visible()

    new_tab.close()

# Alternative approach using class and fixture to avoid opening the page multiple times for each test

# class TestA:
#     @pytest.fixture(scope="class", autouse=True)
#     def setup_class(self, app):
#         self.page = app.links.new_tab_link_page
#         self.page.open()
#
#         yield
#
#     def test_new_tab_link_opens_in_new_tab(self):
#         with self.page.page.expect_popup() as popup_info:
#             self.page.click_link()
#
#         self.another_page = popup_info.value
#         self.another_page.wait_for_load_state()
#         expect(self.another_page).to_have_url("https://www.qa-practice.com/elements/new_tab/new_page")
#
#         result_text = self.another_page.locator("#result-text")
#         expect(result_text).to_have_text("I am a new page in a new tab")
#         expect(result_text).to_be_visible()