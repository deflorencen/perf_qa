HOST = "https://www.qa-practice.com/"

class Urls:
    class Elements:

        class Buttons:
            SIMPLE = f"{HOST}elements/button/simple"
            DISABLED = f"{HOST}elements/button/disabled"
            LIKE_A_BUTTON = f"{HOST}elements/button/like_a_button"

        class Inputs:
            SIMPLE = f"{HOST}elements/input/simple"
            EMAIL = f"{HOST}elements/input/email"
            PASSWORD = f"{HOST}elements/input/passwd"

        class Checkbox:
            SINGLE_CHECKBOX = f"{HOST}elements/checkbox/single_checkbox"
            MULTIPLE_CHECKBOX = f"{HOST}elements/checkbox/mult_checkbox"

        class Selectors:
            SINGLE_SELECT = f"{HOST}elements/select/single_select"
            MULTIPLE_SELECT = f"{HOST}elements/select/mult_select"

        class Links:
            TAB_LINK = f"{HOST}elements/new_tab/link"
            TAB_BUTTON = f"{HOST}elements/new_tab/button"

        class TextArea:
            SIMPLE_TEXT_AREA = f"{HOST}elements/textarea/single"
            MULTIPLE_TEXT_AREA = f"{HOST}elements/textarea/textareas"

        class Alerts:
            ALERT_BOX = f"{HOST}elements/alert/alert#"
            CONFIRM_BOX = f"{HOST}elements/alert/confirm#"