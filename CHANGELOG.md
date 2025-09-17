# Change Log
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [0.5.1] - 2025-09-17
 
### Added
 
### Changed
 
### Fixed
- Import paths

## [0.5.0] - 2025-09-15
  
New functionalities.
 
### Added
- Scraping Module including:
  - **launch_chrome**: Launches a Chrome browser instance with custom settings.
 
### Changed
- Docstring documentation
- Update requirements.txt
- Refactored package and function names:
  - Renamed package string_operations to strings. 
    - Renamed function get_all_file_paths_in_directory to list_files. 
    - Renamed function update_excel_column_from_list to update_excel_column. 
  - Renamed package file_operations to files. 
    - Renamed function find_pattern_in_string to findall_matches.
- Changed all input path variables from str type to Path.
 
### Fixed


## [0.4.0] - 2025-07-30
  
New functionalities.
 
### Added
- File Operations Module including:
  - **update_excel_column_from_list**: Update a specific column in an Excel sheet with values from a list.
 
### Changed
- Docstring documentation
- Update requirements.txt
 
### Fixed


## [0.3.0] - 2025-03-30
  
New functionalities.
 
### Added
- String Operations Module including:
  - **get_substring_between**: Extract all substrings between open_mark and close_mark from input string.
- File Operations Module including:
  - **iterate_hocon**: This function traverses the HOCON configuration structure and yields key-value pairs.
 
### Changed
- Docstring documentation
 
### Fixed
- Delete unnecessary imports


## [0.2.0] - 2024-08-30
  
New functionalities.
 
### Added
- String Operations Module including:
  - **find_pattern_in_string**: Find all occurrences of a pattern in a given string using regex.
  - **replace_all**: Replace all occurrences of keys in input dict within input string with their corresponding values.
 
### Changed
 
### Fixed


## [0.1.0] - 2024-07-13
Base Project Structure.
 
### Added
- File Operations Module including:
  - **get_all_file_paths_in_directory**: Retrieve a list of all file paths within a specified folder and its subdirectories.
  - **read_json**: Read and parse a JSON file into a Python dictionary.
  - **write_json**: Serialize a Python dictionary into JSON format and write it to a file.
  - **read_hocon**: Read and parse a HOCON file into a Python dictionary.
  - **write_hocon**: Serialize a Python dictionary into HOCON format and write it to a file.
   
### Changed
 
### Fixed
