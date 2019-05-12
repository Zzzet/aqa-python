from sel.pages.create_issue_page import CreateIssuePage
from sel.pages.home_page import HomePage
from sel.pages.issue_page import IssuePage

from sel.pages.login_page import LoginPage
from selenium_tests.test_base import BaseTest


class TestJira(BaseTest):

    def test_login(self):
        LoginPage().open() \
            .enter_username("DmytroKarpenko") \
            .enter_password("DmytroKarpenko") \
            .click_login()

    # no such issue reporter = DmytroKarpenko and status = Resolved

    # 5 issues reporter = currentUser() and summary ~  "upd-123"

    # 1 issue reporter = currentUser() and summary ~  "upd-123"