import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.sel.elements.base_element import BaseElement
from src.sel.pages.base_page import BasePage


class CreateIssuePopup(BasePage):

    @allure.step
    def set_project(self, name):
        BaseElement((By.ID, "project-field")).send(name).send(Keys.TAB)
        return self

    @allure.step
    def set_issue_type(self, type):
        BaseElement((By.ID, "issuetype-field")).send(type).send(Keys.TAB)
        return self

    @allure.step
    def set_summary(self, summary):
        BaseElement((By.ID, "summary")).send(summary).send(Keys.TAB)
        return self

    @allure.step
    def set_assignee(self, assignee):
        BaseElement((By.ID, "assignee-field")).send(assignee).send(Keys.TAB)
        return self

    @allure.step
    def set_priority(self, assignee):
        BaseElement((By.ID, "priority-field")).send(assignee).send(Keys.TAB)
        return self

    @allure.step
    def click_submit_btn(self):
        BaseElement((By.ID, "create-issue-submit")).scroll_to().click()
        return self

    @allure.step
    def click_update_btn(self):
        BaseElement((By.ID, "edit-issue-submit")).scroll_to().click()
        return self

