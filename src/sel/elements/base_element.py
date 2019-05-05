from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from util.driver_container import DriverContainer


class BaseElement:
    timeout = 10


    def __init__(self, selector):
        self.selector = selector
        self.driver = DriverContainer().get_driver(DriverContainer)
        return

    def wait_until_present(self)-> WebElement:
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(self.selector))
        return element
