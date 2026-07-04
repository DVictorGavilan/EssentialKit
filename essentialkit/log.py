import logging.config

from pathlib import Path
from essentialkit.files import read_json


def configure(path: Path, logs_dir: Path = Path("logs")) -> None:
    """
    This function configures Python logging using a JSON configuration.

    :param path: The path to the JSON file containing the logging configuration
    :param logs_dir: The directory where log files will be stored. Defaults to "logs"
    :return: None
    """
    logs_dir.mkdir(parents=True, exist_ok=True)
    logging_config = read_json(path=path)
    logging.config.dictConfig(logging_config)
