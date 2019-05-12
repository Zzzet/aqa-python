from selenium.webdriver.common.by import By

from sel.elements.base_element import BaseElement
from sel.pages.create_issue_page import CreateIssuePage
from sel.pages.notification import Notification
from sel.pages.header import Header
from util.driver_container import DriverContainer


class IssuePage:
    notification = Notification()
    header = Header()

    def __init__(self):
        self.driver = DriverContainer().get_driver(DriverContainer)

    def click_edit_btn(self):
        BaseElement((By.ID, "edit-issue")).wait_until_clickable().click()

    def click_more_btn(self):
        BaseElement((By.ID, "opsbar-operations_more")).wait_until_clickable().click()
        return self

    def click_delete(self):
        BaseElement((By.ID, "delete-issue")).wait_until_clickable().click()
        return self
