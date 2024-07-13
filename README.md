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

## How to use it
Install the library

```bash
pip install essentialkit
```


## Functionalities
- **get_all_file_paths_in_directory**: Retrieve a list of all file paths within a specified folder and its subdirectories.
- **read_json**: Read and parse a JSON file into a Python dictionary.
- **write_json**: Serialize a Python dictionary into JSON format and write it to a file.
- **read_hocon**: Read and parse a HOCON file into a Python dictionary.
- **write_hocon**: Serialize a Python dictionary into HOCON format and write it to a file.