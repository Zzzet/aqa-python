from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager

from sel.pages.create_issue_page import CreateIssuePage
from sel.pages.home_page import HomePage
from sel.pages.login_page import LoginPage
from selenium_tests.test_base import BaseTest


class TestJira(BaseTest):

    # def test_f(self):
    #     self.driver.get("http://www.python.org")
    #     assert "Python" in self.driver.title
    #     elem = self.driver.find_element_by_name("q")
    #     elem.send_keys("pycon")
    #     elem.send_keys(Keys.RETURN)
    #     assert "No results found." not in self.driver.page_source

    def test_login(self):
       LoginPage().open()\
            .enter_username("DmytroKarpenko")\
            .enter_password("DmytroKarpenko")\
            .click_login()

       HomePage().header.click_create_btn()
       CreateIssuePage().set_project("Webinar")