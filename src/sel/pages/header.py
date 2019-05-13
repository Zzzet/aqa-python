import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from sel.elements.base_element import BaseElement
from sel.pages.BasePage import BasePage
from util.driver_container import DriverContainer


class Header(BasePage):

    def __init__(self):
        self.driver = DriverContainer().get_driver(DriverContainer)

    def click_create_btn(self, ):
        self.backdrop_dissapears()
        BaseElement((By.ID, "create_link")).wait_until_clickable().click()
        return self

    def open_search(self, ):
        self.backdrop_dissapears()
        BaseElement((By.ID, "quickSearchInput")).wait_until_clickable().click()
        BaseElement((By.ID, "quickSearchInput")).wait_until_clickable().send_keys(Keys.ENTER)
        return self
