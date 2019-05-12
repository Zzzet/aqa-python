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

        HomePage().header.click_create_btn()

        CreateIssuePage().set_project("Webinar") \
            .set_issue_type("Story") \
            .set_summary("My issue") \
            .click_submit_btn()

        HomePage().notification.open_issue()

        IssuePage().click_edit_btn()

        CreateIssuePage().set_summary("upd") \
            .set_assignee("DmytroKarpenko") \
            .set_priority("High") \
            .click_update_btn()
