import re
from re import error


def find_pattern_in_string(input_string: str, pattern: str) -> list:
    """
    Find all occurrences of a pattern in a given string using regex.

    :param input_string: The string in which to search for the pattern
    :param pattern: The regex pattern to search for
    :return: A list of all matches found
    """
    try:
        compiled_pattern = re.compile(pattern)
        matches = compiled_pattern.findall(input_string)
        return matches
    except TypeError:
        raise TypeError("Arguments must be str")
    except error as e:
        raise ValueError(f"Invalid regex pattern: {e}")


def replace_all(input_string: str, replace_values: dict) -> str:
    """
    This function iterates over each key-value pair in the `replace_values` dictionary and replaces
    every occurrence of the key in `input_string` with the corresponding value.

    :param input_string: The input string in which replacements are to be made
    :param replace_values: A dictionary where each key is a substring to be replaced,
    and each value is the substring to replace the key with
    :return: A new string with all the replacements made
    """
    for key, value in replace_values.items():
        input_string = input_string.replace(key, value)
    return input_string


def get_substring_between(string: str, open_mark: str, close_mark: str) -> list[str]:
    """
    Extract all substrings between open_mark and close_mark using f-strings

    :param string: The input string to search within
    :param open_mark: The opening delimiter marking the start of the substring
    :param close_mark: The closing delimiter marking the end of the substring
    :return: A list of substrings found between the given markers
    """
    pattern = fr"{re.escape(open_mark)}(.*?){re.escape(close_mark)}"
    return re.findall(pattern, string)
