from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.sel.pages.base_page import BasePage
from src.sel.elements.base_element import BaseElement
from src.sel.widgets.header import Header
from src.util.driver_container import DriverContainer


class CreateIssuePage(BasePage):

    def __init__(self):
        self.driver = DriverContainer().get_driver(DriverContainer)

    def set_project(self, name):
        BaseElement((By.ID, "project-field")).set_value(name)
        return self

    def set_issue_type(self, type):
        BaseElement((By.ID, "issuetype-field")).set_value(type)
        return self

    def set_summary(self, summary):
        BaseElement((By.ID, "summary")).set_value(summary)
        return self

    def set_assignee(self, assignee):
        BaseElement((By.ID, "assignee-field")).set_value(assignee)
        return self

    def set_priority(self, assignee):
        BaseElement((By.ID, "priority-field")).set_value(assignee)
        return self

    def click_submit_btn(self):
        BaseElement((By.ID, "create-issue-submit")).click()
        self.backdrop_dissapears()
        return self

    def click_update_btn(self):
        BaseElement((By.ID, "edit-issue-submit")).click()
        self.backdrop_dissapears()
        return self

    def get_summary(self):
        return BaseElement((By.ID, "summary-val")).wait_until_ready().text

    def get_assignee(self):
        return BaseElement((By.ID, "assignee-val")).wait_until_ready().text

    def get_priority(self):
        return BaseElement((By.ID, "priority-val")).wait_until_ready().text
