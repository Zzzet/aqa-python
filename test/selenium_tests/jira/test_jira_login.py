from src.sel.pages.create_issue_page import CreateIssuePopup
from src.sel.pages.home_page import HomePage
from src.sel.pages.issue_details_page import IssuePage

from src.sel.pages.login_page import LoginPage
from test.selenium_tests.test_base import BaseTest


class TestJiraLogin(BaseTest):


    def test_login_successfull(self):
        LoginPage().open() \
            .login_as("DmytroKarpenko", "DmytroKarpenko")
        intro = HomePage().introduction_text()
        assert intro.__contains__("Welcome to Hillel IT School JIRA")

    def test_login_wrong_name(self):
        error = LoginPage().open() \
            .enter_username("DmytroKarpenko") \
            .enter_password("wrong") \
            .click_login().get_aui_error()
        assert error.__contains__("Sorry, your username and password are incorrect - please try again.")

    def test_login_wrong_password(self):
        error = LoginPage().open() \
            .enter_username("wrong") \
            .enter_password("DmytroKarpenko") \
            .click_login().get_aui_error()
        assert error.__contains__("Sorry, your username and password are incorrect - please try again.")
