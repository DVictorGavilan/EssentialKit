import pytest

from pathlib import Path
from assertpy import assert_that
from unittest.mock import patch, MagicMock
from selenium.webdriver.chrome.webdriver import WebDriver
from essentialkit.scraping import launch_chrome


@pytest.fixture
def mock_chrome_driver():
    """Mock Chrome WebDriver to avoid launching a real browser."""
    with patch("essentialkit.scraping.webdriver.Chrome") as mock_driver_class:
        mock_driver = MagicMock(spec=WebDriver)
        mock_driver_class.return_value = mock_driver
        yield mock_driver, mock_driver_class


@pytest.fixture
def mock_chrome_service():
    """Mock ChromeDriverManager install method to avoid downloading chromedriver."""
    with patch("essentialkit.scraping.ChromeDriverManager.install") as mock_install:
        mock_install.return_value = "/fake/path/to/chromedriver"
        yield mock_install


@pytest.fixture
def mock_tempfile_mkdtemp():
    """Mock tempfile.mkdtemp to return a predictable temporary directory."""
    with patch("essentialkit.scraping.tempfile.mkdtemp") as mock_mkdtemp:
        mock_mkdtemp.return_value = "/tmp/fake_profile"
        yield mock_mkdtemp


def test_launch_chrome_returns_webdriver(
    mock_chrome_driver, mock_chrome_service, mock_tempfile_mkdtemp, tmp_path
):
    mock_driver, _ = mock_chrome_driver
    download_dir = tmp_path / "downloads"

    driver = launch_chrome(download_dir)

    # The returned object is the mocked WebDriver
    assert_that(driver).is_equal_to(mock_driver)


def test_launch_chrome_creates_download_directory(
    mock_chrome_driver, mock_chrome_service, mock_tempfile_mkdtemp, tmp_path
):
    download_dir = tmp_path / "downloads"

    # Directory should not exist before call
    assert_that(download_dir.exists()).is_false()

    launch_chrome(download_dir)

    # Directory should be created
    assert_that(download_dir.exists()).is_true()


def test_launch_chrome_sets_download_preferences(
    mock_chrome_driver, mock_chrome_service, mock_tempfile_mkdtemp
):
    mock_driver, mock_driver_class = mock_chrome_driver
    download_dir = Path("/tmp/downloads")

    launch_chrome(download_dir)

    # Retrieve ChromeOptions argument passed to webdriver.Chrome
    _, kwargs = mock_driver_class.call_args
    chrome_options = kwargs.get("options")
    prefs = chrome_options.experimental_options.get("prefs")

    assert_that(prefs["download.default_directory"]).is_equal_to(str(download_dir.resolve()))
    assert_that(prefs["download.prompt_for_download"]).is_false()
    assert_that(prefs["directory_upgrade"]).is_true()


def test_launch_chrome_adds_expected_arguments(
    mock_chrome_driver, mock_chrome_service, mock_tempfile_mkdtemp
):
    mock_driver, mock_driver_class = mock_chrome_driver
    download_dir = Path("/tmp/downloads")

    launch_chrome(download_dir)

    _, kwargs = mock_driver_class.call_args
    chrome_options = kwargs.get("options")
    arguments = chrome_options.arguments

    assert_that(arguments).contains("--disable-blink-features=AutomationControlled")
    assert_that(arguments).contains("--start-maximized")
    assert_that(arguments).contains("--force-device-scale-factor=0.5")
    assert_that(arguments).contains("--user-data-dir=/tmp/fake_profile")
