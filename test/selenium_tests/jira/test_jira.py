from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager

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
       login =  LoginPage()

       login.open()\
            .enter_username("DmytroKarpenko")\
            .enter_password("DmytroKarpenko")\
            .click_login()