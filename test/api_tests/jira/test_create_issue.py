import pytest

from test.api_tests.test_api_base import ApiBaseTest
from src.rest.jira.issue import Issue
from src.util.string_utils import randomString


class TestCreateIssue(ApiBaseTest):

    def test_create_issue(self):
        issue = Issue() \
            .set_issue_type("Bug") \
            .set_project("WEBINAR") \
            .set_summary("abc123") \
            .set_description("blah") \
            .post()

        assert issue.status_code == 201, "Status code should be correct"
        issue.get()
        assert issue.status_code == 200, "Status code should be correct"

    def test_create_issue_missing_field(self):
        issue = Issue() \
            .set_issue_type("Bug") \
            .set_summary("abc123") \
            .set_description("blah") \
            .post()
        assert issue.status_code == 400, "Status code should be correct"

    def test_create_issue_long_field(self):
        long_summary = randomString(256)
        issue = Issue() \
            .set_issue_type("Bug") \
            .set_project("WEBINAR") \
            .set_summary(long_summary) \
            .set_description("blah") \
            .post()
        assert issue.status_code == 400, "Status code should be correct"
