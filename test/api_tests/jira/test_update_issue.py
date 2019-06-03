import pytest

from test.api_tests.test_api_base import ApiBaseTest
from src.rest.jira.issue import Issue


class TestUpdateIssue(ApiBaseTest):

    def test_update_assignee(self, create_api_issue):
        issue_to_update = Issue()
        issue_to_update.key = create_api_issue.key
        issue_to_update.set_assignee("DmytroKarpenko")
        issue_to_update.put()
        assert issue_to_update.status_code == 204, "Status code should be correct"
        issue_to_update.get()
        assert issue_to_update.response["fields"]["assignee"]["name"] == "DmytroKarpenko", "assignee should be updated"


    def test_update_priority(self, create_api_issue):
        issue_to_update = Issue()
        issue_to_update.key = create_api_issue.key
        issue_to_update.set_priority("Lowest")
        issue_to_update.put()
        assert issue_to_update.status_code == 204, "Status code should be correct"
        issue_to_update.get()
        assert issue_to_update.response["fields"]["priority"]["name"] == "Lowest", "priority should be updated"

    def test_update_summary(self, create_api_issue):
        issue_to_update = Issue()
        issue_to_update.key = create_api_issue.key
        issue_to_update.set_summary("updated summary")
        issue_to_update.put()
        assert issue_to_update.status_code == 204, "Status code should be correct"
        issue_to_update.get()
        assert issue_to_update.response["fields"]["summary"] == "updated summary", "summary should be updated"


