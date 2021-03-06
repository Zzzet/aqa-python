import allure
from selenium.webdriver.common.by import By

from src.sel.elements.base_element import BaseElement
from src.sel.pages.base_page import BasePage


class Notification(BasePage):

    @allure.step
    def open_issue(self):
        self.backdrop_dissapears()
        BaseElement((By.CSS_SELECTOR, "[data-issue-key]")).click()
