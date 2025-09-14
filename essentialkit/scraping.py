import tempfile

from pathlib import Path
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver


def launch_chrome(download_directory: Path) -> WebDriver:
    """
    Launches a Chrome browser instance with custom settings.

    :param download_directory: Path where downloaded files will be stored
    :return: Configured Chrome WebDriver instance.
    """

    download_directory.mkdir(parents=True, exist_ok=True)

    chrome_service = Service(ChromeDriverManager().install())
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--force-device-scale-factor=0.5")
    chrome_options.add_experimental_option(
        name="prefs",
        value={
            "download.default_directory": str(download_directory.resolve()),
            "download.prompt_for_download": False,
            "directory_upgrade": True
        }
    )

    # Use a unique temporary user profile to avoid conflicts
    unique_profile = tempfile.mkdtemp()
    chrome_options.add_argument(f"--user-data-dir={unique_profile}")

    driver = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return driver
