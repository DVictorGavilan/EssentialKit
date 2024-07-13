import json
import pytest

from assertpy import assert_that
from essentialkit import file_operations
from pyparsing import ParseSyntaxException
from pyhocon import HOCONConverter, ConfigFactory


@pytest.fixture
def create_valid_json_file(tmp_path):
    file_path = tmp_path / "data.json"
    data = {"key": "value"}
    with open(file_path, "w") as file:
        json.dump(data, file)
    return str(file_path)


@pytest.fixture
def create_invalid_file(tmp_path):
    file_path = tmp_path / "invalid_data"
    with open(file_path, "w") as file:
        file.write("invalid content")
    return str(file_path)


@pytest.fixture
def create_valid_txt_file(tmp_path):
    file_path = tmp_path / "data.txt"
    with open(file_path, "w") as file:
        file.write("This is text file")
    return str(file_path)


@pytest.fixture
def create_valid_hocon_file(tmp_path):
    file_path = tmp_path / "data.conf"
    data = {"key": "value"}
    data_parsed = ConfigFactory.from_dict(data)
    with open(file_path, "w") as file:
        file.write(HOCONConverter.to_hocon(data_parsed))
    return str(file_path)


@pytest.fixture
def output_path(tmp_path):
    return tmp_path / "test_output.json"


@pytest.fixture
def create_folder_structure(tmpdir):
    folder_path = tmpdir.mkdir("test_folder")
    sub_folder_path = folder_path.mkdir("sub_folder_path")

    folder_file = folder_path.join("folder_file.txt")
    with open(folder_file, "w") as file:
        file.write("Content in file 1")

    sub_folder_file = sub_folder_path.join("sub_folder_file.txt")
    with open(sub_folder_file, "w") as file:
        file.write("Content in file 2")

    return str(folder_path)


def test_receive_a_valid_folder_with_files(create_folder_structure):
    folder_path = create_folder_structure
    result = file_operations.get_all_file_paths_in_directory(folder_path)
    assert_that(result[0]).is_named("folder_file.txt")
    assert_that(result[1]).is_named("sub_folder_file.txt")
    all(assert_that(file_path).is_file() for file_path in result)


def test_receive_an_empty_folder(tmpdir):
    folder_path = tmpdir.mkdir("empty_folder")
    assert_that(file_operations.get_all_file_paths_in_directory(folder_path)).is_equal_to([])


def test_invalid_folder_path():
    assert_that(file_operations.get_all_file_paths_in_directory).raises(OSError).when_called_with("nonexistent_folder")


def test_file_path(create_valid_txt_file):
    assert_that(file_operations.get_all_file_paths_in_directory).raises(OSError).when_called_with(create_valid_txt_file)


def test_read_json_receive_a_valid_json_file(create_valid_json_file):
    expected_data = {"key": "value"}
    assert_that(file_operations.read_json(create_valid_json_file)).is_equal_to(expected_data)


def test_read_json_receive_a_invalid_json_file(create_invalid_file):
    assert_that(file_operations.read_json).raises(json.JSONDecodeError).when_called_with(create_invalid_file)


def test_read_json_receive_json_nonexistent_file():
    assert_that(file_operations.read_json).raises(FileNotFoundError).when_called_with("nonexistent_file.json")


def test_read_json_receive_receive_a_txt_file(create_valid_txt_file):
    assert_that(file_operations.read_json).raises(json.JSONDecodeError).when_called_with(create_valid_txt_file)


def test_write_json_data_successfully(output_path):
    test_data = {"key1": "value1", "key2": 2, "key3": [1, 2, 3]}
    file_operations.write_json(test_data, str(output_path))
    with open(output_path, "r") as file:
        written_data = json.load(file)
    assert_that(written_data).is_equal_to(test_data)


def test_write_json_data_sorting_keys(output_path):
    test_data = {"b": 2, "a": 1}
    file_operations.write_json(test_data, str(output_path), sort_keys=True)
    with open(output_path, "r") as file:
        written_data = json.load(file)
    assert_that(written_data).is_equal_to(test_data)


def test_write_json_invalid_input(output_path):
    assert_that(file_operations.write_json).raises(TypeError).when_called_with("not a dict")


def test_write_json_invalid_output_path():
    invalid_path = "/invalid/output.json"
    assert_that(file_operations.write_json).raises(FileNotFoundError).when_called_with({"key": "value"}, invalid_path)


def test_read_hocon_receive_a_valid_hocon_file(create_valid_hocon_file):
    expected_data = {"key": "value"}
    assert_that(file_operations.read_hocon(create_valid_hocon_file, True)).is_equal_to(expected_data)


def test_read_hocon_receive_a_invalid_hocon_file(create_invalid_file):
    assert_that(file_operations.read_hocon).raises(ParseSyntaxException).when_called_with(create_invalid_file, False)


def test_read_hocon_receive_nonexistent_file():
    assert_that(file_operations.read_hocon).raises(FileNotFoundError).when_called_with("nonexistent_file.conf", False)


def test_read_hocon_receive_a_txt_file(create_valid_txt_file):
    assert_that(file_operations.read_hocon).raises(ParseSyntaxException).when_called_with(create_valid_txt_file, False)


def test_write_hocon_data_successfully(output_path):
    test_data = {"key1": "value1", "key2": 2, "key3": [1, 2, 3]}
    file_operations.write_hocon(test_data, str(output_path))
    written_data = ConfigFactory.parse_file(output_path)
    assert_that(written_data).is_equal_to(test_data)


def test_write_hocon_invalid_input(output_path):
    assert_that(file_operations.write_hocon).raises(TypeError).when_called_with("not a dict")


def test_write_hocon_invalid_output_path():
    invalid_path = "/invalid/output.json"
    assert_that(file_operations.write_hocon).raises(FileNotFoundError).when_called_with({"key": "value"}, invalid_path)
