# EssentialKit

## Functional Description
A  comprehensive utility package to simplify common tasks in Python programming

## Owner
For any bugs or questions, please reach out to [Dani Gavilán](mailto:danigavipedro96@gmail.com)

## Branching Methodology
This project follows a Git Flow simplified branching methodology
- **Master Branch**: production code
- **Develop Branch**: main integration branch for ongoing development. Features and fixes are merged into this branch before reaching master
- **Feature Branch**: created from develop branch to work on new features

## Prerequisites
This project uses:
- Language: Python 3.10
- Libraries: 
  - pyhocon
  - pytest
  - assertpy
  - selenium

## How to use it
Install the library

```bash
pip install essentialkit
```

```bash
directory: Path = "/home/user/Documents/test/"

files: list[Path] = essentialkit.files.list_files(path=directory)

```


## Functionalities
### File Module
- **list_files**: Retrieve a list of all file paths within a specified folder and its subdirectories.
- **read_json**: Read and parse a JSON file into a Python dictionary.
- **write_json**: Serialize a Python dictionary into JSON format and write it to a file.
- **read_hocon**: Read and parse a HOCON file into a Python dictionary.
- **iterate_hocon**: Read nested dictionaries and lists into dot and index generator.
- **write_hocon**: Serialize a Python dictionary into HOCON format and write it to a file.
- **update_excel_column**: Update a specific column in an Excel sheet with values from a list.
### String Module
- **find_pattern_in_string**: Find all occurrences of a pattern in a given string using regex.
- **replace_all**: Replace all occurrences of keys in input dict within input string with their corresponding values.
 ### Scraping Module
- **launch_chrome**: Launches a Chrome browser instance with custom settings.
 