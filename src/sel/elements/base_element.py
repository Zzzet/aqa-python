from typing import List

from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException, \
    NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.util.driver_container import DriverContainer


class BaseElement:
    timeout = 20
    driver: WebDriver

    def __init__(self, selector):
        self.selector = selector
        self.driver = DriverContainer().get_driver(DriverContainer)
        return

    def wait_until_ready(self) -> WebElement:
        element = WebDriverWait(self.driver, self.timeout,
                                ignored_exceptions=(ElementClickInterceptedException,
                                                    ElementNotVisibleException,
                                                    NoSuchElementException,
                                                    StaleElementReferenceException)).until(
            EC.element_to_be_clickable(self.selector))
        return element

    def wait_until_visible(self) -> WebElement:
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.selector))
        return element

    def wait_until_present(self) -> WebElement:
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(self.selector))
        return element

    def wait_until_not_visible(self) -> WebElement:
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.invisibility_of_element(self.selector))
        return element

    def get_list(self) -> List[WebElement]:
        elements = self.driver.find_elements(self.selector[0], self.selector[1])
        return elements

