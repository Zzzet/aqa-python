from selenium.webdriver.common.by import By

from sel.elements.base_element import BaseElement
from sel.pages.header import Header
from util.driver_container import DriverContainer


class HomePage:

    header = Header()
    def __init__(self):
        self.driver = DriverContainer().get_driver(DriverContainer)

