from selenium.webdriver.common.by import By

from src.sel.elements.base_element import BaseElement
from src.sel.pages.base_page import BasePage
from src.sel.widgets.header import Header
from src.sel.widgets.notification import Notification
from src.util.driver_container import DriverContainer


class HomePage(BasePage):
    notification = Notification()
    header = Header()

    def introduction_text(self) -> str:
        return BaseElement((By.CSS_SELECTOR, "#gadget-10000")).get_value()
