import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


# host = pytest.config.getoption("-H")
# port = pytest.config.getoption("-P")


class DriverContainer:
    driver = None

    @staticmethod
    def get_driver(cls) -> WebDriver:
        return cls.driver

    @staticmethod
    def create_driver(cls):
        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    @staticmethod
    def create_driver_remote(cls):
        host = pytest.config.getoption("-H")
        port = pytest.config.getoption("-P")
        cls.driver = webdriver.Remote(
            desired_capabilities=webdriver.DesiredCapabilities.CHROME,
            command_executor=f"http://{host}:{port}/wd/hub"

        )
