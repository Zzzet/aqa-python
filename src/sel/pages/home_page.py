from selenium.webdriver.common.by import By

from src.sel.widgets.notification import Notification
from src.sel.widgets.header import Header
from src.util.driver_container import DriverContainer

from src.sel.elements.base_element import BaseElement
from src.sel.pages.base_page import BasePage


class HomePage(BasePage):
    notification = Notification()
    header = Header()

    def __init__(self):
        self.driver = DriverContainer().get_driver(DriverContainer)

    def introduction_text(self) -> str:
        return BaseElement((By.CSS_SELECTOR, "#gadget-10000")).wait_until_ready().text
