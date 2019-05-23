import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.sel.elements.base_element import BaseElement
from src.sel.pages.base_page import BasePage
from src.util.driver_container import DriverContainer


class Header(BasePage):

    def __init__(self):
        self.driver = DriverContainer().get_driver(DriverContainer)

    @allure.step
    def click_create_btn(self, ):
        self.backdrop_dissapears()
        BaseElement((By.ID, "create_link")).click()
        return self

    @allure.step
    def open_search(self, ):
        self.backdrop_dissapears()
        BaseElement((By.ID, "quickSearchInput")).click()
        BaseElement((By.ID, "quickSearchInput")).send(Keys.ENTER)
        return self
