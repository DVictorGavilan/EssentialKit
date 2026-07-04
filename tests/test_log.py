import json
import pytest
import logging

from assertpy import assert_that
from essentialkit import log


@pytest.fixture
def clean_root_logger():
    root_logger = logging.getLogger()

    original_handlers = root_logger.handlers[:]
    original_level = root_logger.level

    yield

    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
        handler.close()

    for handler in original_handlers:
        root_logger.addHandler(handler)

    root_logger.setLevel(original_level)


def test_log_configure_with_real_config_writes_logs_to_file(tmp_path, clean_root_logger):
    logs_dir = tmp_path / "logs"
    log_file = logs_dir / "pipeline.log"
    config_path = tmp_path / "logging.json"

    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "detailed": {
                "format": "%(asctime)s [%(levelname)s | %(module)s:%(lineno)d] %(message)s",
                "datefmt": "%Y-%m-%dT%H:%M:%S%z"
            }
        },
        "handlers": {
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "formatter": "detailed",
                "filename": str(log_file),
                "maxBytes": 1000000,
                "backupCount": 5,
                "encoding": "utf8"
            },
        },
        "root": {
            "level": "INFO",
            "handlers": ["file"]
        }
    }

    config_path.write_text(json.dumps(logging_config), encoding="utf-8")

    log.configure(path=config_path, logs_dir=logs_dir)

    logger = logging.getLogger("essentialkit.tests")
    logger.info("Logging integration test message")

    for handler in logging.getLogger().handlers:
        handler.flush()

    assert_that(log_file.exists()).is_true()

    log_content = log_file.read_text(encoding="utf-8")

    log.configure(path=config_path, logs_dir=logs_dir)

    assert_that(log_content).contains("INFO")
    assert_that(log_content).contains("Logging integration test message")
