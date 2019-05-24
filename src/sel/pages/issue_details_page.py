import allure
from selenium.webdriver.common.by import By

from src.sel.elements.base_element import BaseElement
from src.sel.pages.base_page import BasePage
from src.sel.widgets.header import Header
from src.sel.widgets.notification import Notification


class IssuePage(BasePage):
    notification = Notification()
    header = Header()

    def __init__(self):
        self.backdrop_dissapears()

    @allure.step
    def click_edit_btn(self):
        BaseElement((By.ID, "edit-issue")).click()

    @allure.step
    def click_more_btn(self):
        BaseElement((By.ID, "opsbar-operations_more")).click()
        return self

    @allure.step
    def click_delete(self):
        BaseElement((By.ID, "delete-issue")).click()
        return self

    @allure.step
    def get_summary(self) -> str:
        return BaseElement((By.ID, "summary-val")).get_value()

    @allure.step
    def get_assignee(self) -> str:
        return BaseElement((By.ID, "assignee-val")).get_value()

    @allure.step
    def get_priority(self) -> str:
        return BaseElement((By.ID, "priority-val")).get_value()
