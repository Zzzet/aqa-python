import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.sel.elements.base_element import BaseElement
from src.sel.pages.base_page import BasePage
from src.util.driver_container import DriverContainer


class SearchPage(BasePage):
    issue_list = (By.CSS_SELECTOR, "[class='issue-list'] > [data-key]")

    def __init__(self):
        self.driver = DriverContainer().get_driver(DriverContainer)
        self.backdrop_dissapears()

    @allure.step
    def open(self):
        self.driver.get(DriverContainer.base_url + "issues/?jql=")
        self.backdrop_dissapears()
        self.details_loaded()
        return self

    @allure.step
    def enter_query(self, query):
        issues = BaseElement(self.issue_list);
        issue = issues.get_list()[0]
        BaseElement((By.ID, "advanced-search")).send(query).send(Keys.ENTER)
        issues.wait_until_stale(issue)
        return self

    @allure.step
    def click_search_btn(self):
        BaseElement((By.CSS_SELECTOR, "[class*='search-button']")).click()
        return self

    @allure.step
    def get_issue_count(self):
        self.details_loaded()
        issues = (By.CSS_SELECTOR, "[class='issue-list'] > [data-key]")
        BaseElement(issues).wait_until_ready()
        el_list = BaseElement(issues).get_list()
        return len(el_list)

    @allure.step
    def get_search_message(self) -> str:
        self.details_loaded()
        text = BaseElement((By.CSS_SELECTOR, "[class*='results-message']")).get_value()
        return text
