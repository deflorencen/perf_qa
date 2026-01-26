import pytest

def test_single_checkbox_checked_flow(app):
    """
        Scenario: Checkbox selected -> Submit
        Checks:
        1. User can select checkbox
        2. Button is enabled
        3. Result displays the name (label) of the checkbox
    """

    app.checkboxes.single_checkbox_page.open()
    app.checkboxes.single_checkbox_page.checkbox_should_be_present_once()
    app.checkboxes.single_checkbox_page.submit_should_be_enabled()
    app.checkboxes.single_checkbox_page.checkbox_should_have_label("Select me or not")

    app.checkboxes.single_checkbox_page.check_checkbox()
    app.checkboxes.single_checkbox_page.submit_checkbox()
    app.checkboxes.single_checkbox_page.result_should_be("select me or not")
   


def test_single_checkbox_unchecked_flow(app):
    """
        Scenario: Checkbox NOT selected -> Submit
        Checks:
        1. Checkbox is not selected
        2. Button is enabled (Always enabled requirement)
        3. Result is NOT displayed
    """

    app.checkboxes.single_checkbox_page.open()
    app.checkboxes.single_checkbox_page.checkbox_should_be_present_once()
    app.checkboxes.single_checkbox_page.submit_should_be_enabled()
    app.checkboxes.single_checkbox_page.checkbox_should_have_label("Select me or not")

    app.checkboxes.single_checkbox_page.uncheck_checkbox()
    app.checkboxes.single_checkbox_page.submit_checkbox()
    app.checkboxes.single_checkbox_page.result_should_not_be_visible()