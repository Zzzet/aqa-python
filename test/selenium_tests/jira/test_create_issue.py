import pytest

from src.sel.pages.create_issue_page import CreateIssuePage
from src.sel.pages.home_page import HomePage
from src.sel.pages.issue_details_page import IssuePage
from src.util.string_utils import randomString

from src.sel.pages.login_page import LoginPage
from test.selenium_tests.test_base import BaseTest


@pytest.mark.usefixtures("default_login")
class TestCreateIssues(BaseTest):

    def test_create_issue(self):
        HomePage().header.click_create_btn()
        CreateIssuePage().set_project("Webinar") \
            .set_issue_type("Story") \
            .set_summary("My issue") \
            .click_submit_btn()

    def test_create_with_missing_field(self):
        HomePage().header.click_create_btn()
        error = CreateIssuePage().set_project("Webinar") \
            .set_issue_type("Story") \
            .click_submit_btn().get_error()
        assert error.__contains__("You must specify a summary of the issue.")

    def test_create_with_long_field(self):
        HomePage().header.click_create_btn()
        long_summary = randomString(256)
        error = CreateIssuePage().set_project("Webinar") \
            .set_issue_type("Story") \
            .set_summary(long_summary) \
            .click_submit_btn().get_error()
        assert error.__contains__("Summary must be less than 255 characters.")

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