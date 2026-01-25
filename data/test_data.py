import pytest


class EmailData:
    VALID_EMAILS = [
        pytest.param("test@example.com", id="standard email"),
        pytest.param("test@example.com", id="standard_email"),
        pytest.param("user.name@test-domain.com", id="dots_in_local"),
        pytest.param("test@localhost", id="localhost_domain"),
        pytest.param("user@домен.com", id="cyrillic_domain"),
    ]

    INVALID_EMAILS = [
        pytest.param("", id="empty"),
        pytest.param("plainaddress", id="no_at_symbol"),
        pytest.param("@example.com", id="no_local_part"),
        pytest.param("user@", id="no_domain"),
        pytest.param("user domain@test.com", id="has_space"),
    ]

class Constraints:
    PASS_MIN_LEN = 8

class PasswordData:
    VALID_PASSWORDS = [
        pytest.param("Abcdef1!", id="standard_complexity"),
        pytest.param("StrongPass1$", id="with_dollar_sign"),
        pytest.param("P@ssword123", id="common_pattern_valid"),
        pytest.param("Qwerty9*", id="keyboard_pattern"),
        pytest.param("Aa1!Aa1!", id="repeated_blocks"),
    ]

    INVALID_PASSWORDS = [
        pytest.param("", id="empty_password"),
        pytest.param("short1!", id="too_short"),
        pytest.param("alllowercase1!", id="missing_uppercase"),
        pytest.param("ALLUPPERCASE1!", id="missing_lowercase"),
        pytest.param("NoDigits!", id="missing_digits"),
        pytest.param("NoSpecial1", id="missing_special_char"),
        pytest.param("12345678!", id="missing_letters"),
        pytest.param("abcdefgh", id="missing_digits_and_special"),
    ]

class SimpleInputData:
    MIN_LEN = 2
    MAX_LEN = 25

    VALID_TEXTS = [
        pytest.param("ab", id="min_length_boundary"),
        pytest.param("hello_123", id="alphanumeric_underscore"),
        pytest.param("a" * MAX_LEN, id="max_length_boundary"),
        pytest.param("test-user_01", id="hyphen_and_underscore"),
    ]

    INVALID_TEXTS = [
        pytest.param("", id="empty_required"),
        pytest.param("a", id="below_min_length"),
        pytest.param("a" * (MAX_LEN + 1), id="above_max_length"),
        pytest.param("hello!!!", id="invalid_special_chars"),
        pytest.param("привет", id="cyrillic_chars"),
    ]