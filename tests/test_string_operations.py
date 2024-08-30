from assertpy import assert_that
from essentialkit.string_operations import find_pattern_in_string, replace_all


def test_find_pattern_once_in_string():
    string = "asv1.0.0asdf.334.23"
    regex = "[A-Za-z]{1}[0-9][.][0-9].[0-9]"
    expected = ["v1.0.0"]
    actual = find_pattern_in_string(input_string=string, pattern=regex)
    assert_that(actual).is_equal_to(expected)


def test_find_pattern_multiple_times_in_string():
    string = "asv1.0.0asdf.334.23v2.0.0"
    regex = "[A-Za-z]{1}[0-9][.][0-9].[0-9]"
    expected = ["v1.0.0", "v2.0.0"]
    actual = find_pattern_in_string(input_string=string, pattern=regex)
    assert_that(actual).is_equal_to(expected)


def test_find_pattern_in_empty_string():
    string = ""
    regex = "[A-Za-z]{1}[0-9][.][0-9].[0-9]"
    actual = find_pattern_in_string(input_string=string, pattern=regex)
    assert_that(actual).is_empty()


def test_dont_find_pattern_in_string():
    string = "asv.2.00.0asdf.334.23"
    regex = "[A-Za-z]{1}[0-9][.][0-9].[0-9]"
    actual = find_pattern_in_string(input_string=string, pattern=regex)
    assert_that(actual).is_empty()


def test_special_characters():
    result = find_pattern_in_string("hello. world? yes!", r"\w+")
    assert_that(result).is_equal_to(["hello", "world", "yes"])


def test_invalid_pattern():
    string = 123
    regex = r"(\w+"
    msg_error = "Invalid regex pattern"
    assert_that(find_pattern_in_string).raises(ValueError).when_called_with(string, regex).starts_with(msg_error)


def test_input_string_not_str():
    string = 123
    regex = "[A-Za-z]{1}[0-9][.][0-9].[0-9]"
    msg_error = "Arguments must be str"
    assert_that(find_pattern_in_string).raises(TypeError).when_called_with(string, regex).is_equal_to(msg_error)


def test_pattern_is_not_str():
    string = "asv.2.00.0asdf.334.23"
    regex = 123
    msg_error = "Arguments must be str"
    assert_that(find_pattern_in_string).raises(TypeError).when_called_with(string, regex).is_equal_to(msg_error)


def test_replace_all_with_multiple_replacements():
    result = replace_all("foo bar baz", {"foo": "oof", "bar": "rab"})
    assert_that(result).is_equal_to("oof rab baz")


def test_replace_all_without_matches():
    result = replace_all("unchanged", {"key": "value"})
    assert_that(result).is_equal_to("unchanged")


def test_replace_all_in_an_empty_string():
    result = replace_all("", {"a": "b"})
    assert_that(result).is_equal_to("")


def test_replace_all_without_replacements():
    result = replace_all("unchanged", {})
    assert_that(result).is_equal_to("unchanged")


def test_replace_all_case_sensitive():
    result = replace_all("CaseSensitive", {"case": "CASE", "Sensitive": "Insensitive"})
    assert_that(result).is_equal_to("CaseInsensitive")
