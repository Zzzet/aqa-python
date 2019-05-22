from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.sel.elements.base_element import BaseElement
from src.sel.pages.base_page import BasePage


class CreateIssuePopup(BasePage):

    def set_project(self, name):
        BaseElement((By.ID, "project-field")).set_value(name).set_value(Keys.TAB)
        return self

    def set_issue_type(self, type):
        BaseElement((By.ID, "issuetype-field")).set_value(type).set_value(Keys.TAB)
        return self

    def set_summary(self, summary):
        BaseElement((By.ID, "summary")).set_value(summary).set_value(Keys.TAB)
        return self

    def set_assignee(self, assignee):
        BaseElement((By.ID, "assignee-field")).set_value(assignee).set_value(Keys.TAB)
        return self

    def set_priority(self, assignee):
        BaseElement((By.ID, "priority-field")).set_value(assignee).set_value(Keys.TAB)
        return self

    def click_submit_btn(self):
        BaseElement((By.ID, "create-issue-submit")).click()
        return self

    def click_update_btn(self):
        BaseElement((By.ID, "edit-issue-submit")).click()
        return self

