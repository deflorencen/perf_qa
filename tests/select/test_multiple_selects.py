import pytest, itertools
from playwright.sync_api import expect

def test_multiple_selects_interface(app):
    page = app.selectors.multiple_select_page
    page.open()

    expect(page.label_place).to_have_text("Choose the place you want to go*")
    expect(page.label_transport).to_have_text("Choose how you want to get there*")
    expect(page.label_when).to_have_text("Choose when you want to go*")

    expect(page.dropdown_place).to_have_attribute("required", "")
    expect(page.dropdown_transport).to_have_attribute("required", "")
    expect(page.dropdown_when).to_have_attribute("required", "")

OPTIONS = {
    "places": ["Sea", "Mountains", "Old town", "Ocean", "Restaurant"],
    "transports": ["Car", "Bus", "Train", "Air"],
    "whens": ["Today", "Tomorrow", "Next week"]
}

def generate_all_select_combination():
    test_data = []

    all_combos = list(itertools.product(
        OPTIONS["places"],
        OPTIONS["transports"],
        OPTIONS["whens"]
    ))

    for place, transport, when in all_combos:
        test_id = f"{place}-{transport}-{when}"
        test_data.append(
            pytest.param(place, transport, when, id=test_id)
        )
    return test_data

SELECT_TEST_DATA = generate_all_select_combination()

@pytest.mark.parametrize("place, transport, when", SELECT_TEST_DATA)
def test_form_result_phrase(app, place, transport, when):
    page = app.selectors.multiple_select_page
    page.open()

    page.fill_form(place=place, transport=transport, when=when)
    page.click_submit()

    expected_result = f"to go by {transport} to the {place} {when}".lower()
    expect(page.result_text).to_have_text(expected_result)
    expect(page.result_text).to_be_visible()