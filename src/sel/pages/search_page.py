from selenium.webdriver.common.by import By

from src.sel.elements.base_element import BaseElement
from src.sel.pages.base_page import BasePage
from src.util.driver_container import DriverContainer


class SearchPage(BasePage):

    def __init__(self):
        self.driver = DriverContainer().get_driver(DriverContainer)
        self.backdrop_dissapears()

    def open(self):
        self.driver.get(DriverContainer.base_url+"issues/?jql=")
        self.backdrop_dissapears()
        self.details_loaded()
        return self

    def enter_query(self, query):
        BaseElement((By.ID, "advanced-search")).set_value(query)
        return self

    def click_search_btn(self):
        BaseElement((By.CSS_SELECTOR, "[class*='search-button']")).click()
        return self

    def get_issue_count(self):
        self.details_loaded()
        issues = (By.CSS_SELECTOR, "[class='issue-list'] > [data-key]")
        BaseElement(issues).wait_until_ready()
        el_list = BaseElement(issues).get_list()
        return len(el_list)

    def get_search_message(self) -> str:
        self.details_loaded()
        text = BaseElement((By.CSS_SELECTOR, "[class*='results-message']")).get_value()
        return text
