import random
import string

import pytest

from src.sel.pages.create_issue_page import CreateIssuePopup
from src.sel.widgets.header import Header
from src.sel.pages.search_page import SearchPage
from src.sel.pages.home_page import HomePage
from test.selenium_tests.test_base import BaseTest
from src.util.string_utils import randomString


@pytest.mark.usefixtures("default_login")
class TestJiraSearch(BaseTest):

    def test_search_5_issues(self):
        issue_summary = "My_issue_" + randomString()
        for x in range(5):
            self.create_issue(issue_summary)

        issue_count = SearchPage().open() \
            .enter_query(f"reporter = currentUser() and summary ~  '{issue_summary}'") \
            .get_issue_count()
        assert issue_count == 5, "Issue count should be = 5"

    def test_search_1_issue(self):
        issue_summary = "My_issue_" + randomString()
        self.create_issue(issue_summary)

        issue_count = SearchPage().open() \
            .enter_query(f"reporter = currentUser() and summary ~  '{issue_summary}'") \
            .get_issue_count()
        assert issue_count == 1, "Issue count should be = 1"

    def test_search_no_result(self):
        search_message = SearchPage().open() \
            .enter_query("reporter = currentUser() and status = Canceled") \
            .get_search_message()

        assert search_message.__contains__("No issues were found to match your search"), \
            "Expected message wasn't found"

    def create_issue(self, summary):
        Header().click_create_btn()

        CreateIssuePopup().set_project("Webinar") \
            .set_issue_type("Story") \
            .set_summary(summary) \
            .click_submit_btn()
