from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from sel.elements.base_element import BaseElement
from sel.pages.header import Header
from util.driver_container import DriverContainer


class CreateIssuePage:

    def __init__(self):
        self.driver = DriverContainer().get_driver(DriverContainer)

    def set_project(self, name):
        BaseElement((By.ID, "project-field")).wait_until_visible().send_keys(name)
        BaseElement((By.ID, "project-field")).wait_until_visible().send_keys(Keys.TAB)