import itertools
import pytest

CHECKBOX_MAPPING = {
    0: "one",
    1: "two",
    2: "three"
}

def generate_checkbox_combinations():
    indices = list(CHECKBOX_MAPPING.keys())
    test_data = []

    for r in range(1, len(indices) + 1):
        for combo in itertools.combinations(indices, r):
            sorted_combo = sorted(list(combo))
            expected_text = ", ".join([CHECKBOX_MAPPING[i] for i in sorted_combo])
            test_id = f"check[{expected_text}]"
            test_data.append(
                pytest.param(sorted_combo, expected_text, id=test_id)
            )
    return test_data

COMBINATION_TEST_DATA = generate_checkbox_combinations()

@pytest.mark.parametrize("indices, expected_text", COMBINATION_TEST_DATA)
def test_all_checkbox_combinations(app, indices, expected_text):
    app.checkboxes.multiple_checkbox_page.open()
    app.checkboxes.multiple_checkbox_page.select_checkboxes_by_indices(indices)
    app.checkboxes.multiple_checkbox_page.click_submit()
    app.checkboxes.multiple_checkbox_page.result_should_be(expected_text)
