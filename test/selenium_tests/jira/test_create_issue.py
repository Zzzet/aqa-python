import pytest

from src.sel.pages.create_issue_page import CreateIssuePopup
from src.sel.pages.home_page import HomePage
from src.util.string_utils import randomString
from test.selenium_tests.test_base import BaseTest


@pytest.mark.usefixtures("default_login")
class TestCreateIssues(BaseTest):

    def test_create_issue(self):
        HomePage().header.click_create_btn()
        CreateIssuePopup().set_project("Webinar") \
            .set_issue_type("Story") \
            .set_summary("My issue") \
            .click_submit_btn()

    def test_create_with_missing_field(self):
        HomePage().header.click_create_btn()
        error = CreateIssuePopup().set_project("Webinar") \
            .set_issue_type("Story") \
            .click_submit_btn().get_error()
        assert error.__contains__("You must specify a summary of the issue.")

    def test_create_with_long_field(self):
        HomePage().header.click_create_btn()
        long_summary = randomString(256)
        error = CreateIssuePopup().set_project("Webinar") \
            .set_issue_type("Story") \
            .set_summary(long_summary) \
            .click_submit_btn().get_error()
        assert error.__contains__("Summary must be less than 255 characters.")
