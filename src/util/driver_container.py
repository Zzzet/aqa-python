from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager



class DriverContainer:
    driver = None

    @staticmethod
    def get_driver(cls) -> webdriver:
        return cls.driver

    @staticmethod
    def create_driver(cls):
        cls.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
