from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


class DriverContainer:
    driver = None

    @staticmethod
    def get_driver(cls) -> WebDriver:
        return cls.driver

    @staticmethod
    def create_driver(cls):
        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
