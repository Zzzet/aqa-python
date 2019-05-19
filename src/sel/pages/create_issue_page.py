from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.sel.pages.base_page import BasePage
from src.sel.elements.base_element import BaseElement
from src.sel.pages.header import Header
from src.util.driver_container import DriverContainer


class CreateIssuePage(BasePage):

    def __init__(self):
        self.driver = DriverContainer().get_driver(DriverContainer)

    def set_project(self, name):
        BaseElement((By.ID, "project-field")).wait_until_ready().send_keys(name)
        BaseElement((By.ID, "project-field")).wait_until_ready().send_keys(Keys.TAB)
        return self

    def set_issue_type(self, type):
        BaseElement((By.ID, "issuetype-field")).wait_until_ready().send_keys(type)
        BaseElement((By.ID, "issuetype-field")).wait_until_ready().send_keys(Keys.TAB)
        return self

    def set_summary(self, summary):
        BaseElement((By.ID, "summary")).wait_until_ready().send_keys(summary)
        return self

    def set_assignee(self, assignee):
        BaseElement((By.ID, "assignee-field")).wait_until_ready().send_keys(assignee)
        BaseElement((By.ID, "assignee-field")).wait_until_ready().send_keys(Keys.TAB)
        return self

    def set_priority(self, assignee):
        BaseElement((By.ID, "priority-field")).wait_until_ready().send_keys(assignee)
        BaseElement((By.ID, "priority-field")).wait_until_ready().send_keys(Keys.TAB)
        return self

    def click_submit_btn(self):
        BaseElement((By.ID, "create-issue-submit")).wait_until_ready().click()
        return self

    def click_update_btn(self):
        BaseElement((By.ID, "edit-issue-submit")).wait_until_ready().click()
        return self
