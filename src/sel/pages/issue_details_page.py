from selenium.webdriver.common.by import By

from src.sel.pages.base_page import BasePage
from src.sel.elements.base_element import BaseElement
from src.sel.widgets.header import Header
from src.sel.widgets.notification import Notification
from src.util.driver_container import DriverContainer


class IssuePage(BasePage):
    notification = Notification()
    header = Header()

    def __init__(self):
        self.driver = DriverContainer().get_driver(DriverContainer)

    def click_edit_btn(self):
        BaseElement((By.ID, "edit-issue")).click()

    def click_more_btn(self):
        BaseElement((By.ID, "opsbar-operations_more")).click()
        return self

    def click_delete(self):
        BaseElement((By.ID, "delete-issue")).click()
        return self
