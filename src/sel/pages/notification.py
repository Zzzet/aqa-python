from selenium.webdriver.common.by import By

from sel.elements.base_element import BaseElement


class Notification:
    def open_issue(self):
        BaseElement((By.CSS_SELECTOR, "[class='aui-blanket']")).wait_until_not_visible()
        BaseElement((By.CSS_SELECTOR, "[data-issue-key]")).wait_until_clickable().click()
