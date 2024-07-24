import re
from re import error


def find_pattern_in_string(input_string: str, pattern: str) -> list:
    """
    Find all occurrences of a pattern in a given string using regex.
    :param input_string: The string in which to search for the pattern.
    :param pattern: The regex pattern to search for.
    :return: A list of all matches found.
    """
    try:
        compiled_pattern = re.compile(pattern)
        matches = compiled_pattern.findall(input_string)
        return matches
    except TypeError:
        raise TypeError("Arguments must be str")
    except error as e:
        raise ValueError(f"Invalid regex pattern: {e}")


def match_pattern():
    pass
