import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.sel.elements.base_element import BaseElement
from src.sel.pages.base_page import BasePage
from src.util.driver_container import DriverContainer


class SearchPage(BasePage):

    def __init__(self):
        self.driver = DriverContainer().get_driver(DriverContainer)

    def open(self):
        self.driver.get(DriverContainer.base_url+"issues/?jql=")
        return self

    def enter_query(self, query):
        self.backdrop_dissapears()
        BaseElement((By.ID, "advanced-search")).wait_until_ready().send_keys(query)
        return self

    def click_search_btn(self):
        self.backdrop_dissapears()
        BaseElement((By.CSS_SELECTOR, "[class*='search-button']")).wait_until_ready().click()
        return self

    def get_issue_count(self):
        self.backdrop_dissapears()
        issues = (By.CSS_SELECTOR, "[class='issue-list'] > [data-key]")
        BaseElement(issues).wait_until_ready()
        el_list = BaseElement(issues).get_list()
        return len(el_list)

    def get_search_message(self) -> str:
        self.details_loaded()
        text = BaseElement((By.CSS_SELECTOR, "[class='details-layout']")).wait_until_ready().text
        return text
