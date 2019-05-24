from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


class DriverContainer:
    driver = None
    base_url = None

    @staticmethod
    def get_driver(cls) -> WebDriver:
        return cls.driver

    @staticmethod
    def create_driver(cls, base_url):
        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.base_url = base_url

    @staticmethod
    def close_driver(cls):
        cls.driver.close()
