from selenium.webdriver.common.by import By

from sel.elements.base_element import BaseElement
from sel.pages.BasePage import BasePage


class Notification(BasePage):
    def open_issue(self):
        self.backdrop_dissapears()
        BaseElement((By.CSS_SELECTOR, "[data-issue-key]")).wait_until_clickable().click()
