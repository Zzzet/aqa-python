import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from sel.elements.base_element import BaseElement
from util.driver_container import DriverContainer


class Header:


    def __init__(self):
        self.driver = DriverContainer().get_driver(DriverContainer)

    def click_create_btn(self, ):
        BaseElement((By.CSS_SELECTOR, "[class='aui-blanket']")).wait_until_not_visible()
        BaseElement((By.ID, "create_link")).wait_until_clickable().click()
        return self

    def open_search(self, ):
        BaseElement((By.CSS_SELECTOR, "[class='aui-blanket']")).wait_until_not_visible()
        BaseElement((By.CSS_SELECTOR, "[class='quickSearchInput']")).wait_until_clickable().click()
        BaseElement((By.ID, "quickSearchInput")).wait_until_clickable().send_keys(Keys.ENTER)
        return self