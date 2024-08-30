import os
import json

from pyhocon import HOCONConverter, ConfigTree
from pyhocon.config_parser import STR_SUBSTITUTION, ConfigFactory


def get_all_file_paths_in_directory(path: str) -> list[str]:
    """
    Get a list of all file paths within a specified folder and its subdirectories.

    :param path: The path to the directory to explore
    :return: A list of file paths.
    """
    if not os.path.exists(path):
        raise OSError(f"The specified path '{path}' does not exist.")
    if os.path.isfile(path):
        raise OSError(f"The specified path '{path}' is a file path.")
    return [os.path.join(root, file) for root, _, files in os.walk(path) for file in files]


def read_json(path: str) -> dict:
    """
    Read and parse a JSON file from the given path and return its contents as a Python dictionary.

    :param path: the file path to the JSON file to be read and parsed
    :return: a python dictionary containing the parsed JSON data
    """
    with open(path, mode="r", encoding="utf-8") as file:
        return json.load(file)


def write_json(data: dict, output_path: str, indent: int = 4, sort_keys=False) -> None:
    """
    This function serializes a Python dictionary into JSON format and writes it to the specified
    file.

    :param data: a dictionary containing data to be written to the JSON file
    :param output_path: the file path where the JSON data will be written
    :param indent: the number of spaces used for indentation in the JSON file (default is 4)
    :param sort_keys: whether to sort the keys of the JSON file alphabetically (default is False)
    :return: None
    """
    with open(output_path, 'w') as file:
        json.dump(data, file, indent=indent, sort_keys=sort_keys)


def read_hocon(path: str, replace_env_variables_as_str: bool) -> ConfigTree:
    """
    Read and parse a HOCON file from the given path and return its contents as a Python dictionary.

    :param path: the file path to the HOCON file to be read and parsed
    :param replace_env_variables_as_str: true cast env variables to string
    :return: a python dictionary containing the parsed HOCON data
    """
    if replace_env_variables_as_str:
        return ConfigFactory.parse_file(path, resolve=False, unresolved_value=STR_SUBSTITUTION)
    return ConfigFactory.parse_file(path, resolve=False)


def write_hocon(data: dict, output_path: str, indent: int = 2, compact=True) -> None:
    """
    This function serializes a Python dictionary into HOCON format and writes it to the specified
    file.

    :param data: a dictionary containing data to be written to the HOCON file
    :param output_path: the file path where the HOCON data will be written
    :param indent: the number of spaces used for indentation in the JSON file (default is 2)
    :param compact: whether the key of the dictionary should be compacted (default is True)
    :return: None
    """
    data_parsed = ConfigFactory.from_dict(data)
    with open(output_path, 'w') as conf_file:
        conf_file.write(HOCONConverter.to_hocon(data_parsed, compact=compact, indent=indent))
