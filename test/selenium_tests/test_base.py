import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager

from util.driver_container import DriverContainer


class BaseTest:
    driver = None
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        print("  SETUP")
        DriverContainer().create_driver(DriverContainer)
        yield

        print("  TEARDOWN ")
