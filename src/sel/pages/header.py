from selenium.webdriver.common.by import By

from sel.elements.base_element import BaseElement
from util.driver_container import DriverContainer


class Header:


    def __init__(self):
        self.driver = DriverContainer().get_driver(DriverContainer)

    def click_create_btn(self, ):
        BaseElement((By.ID, "create_link")).wait_until_visible().click()
        return self

