from src.rest.jira.issue import Issue
from src.rest.jira.search import Search
from test.api_tests.test_api_base import ApiBaseTest


class TestSearchIssue(ApiBaseTest):

    def test_search_issue(self, create_api_issue: Issue):
        summary = create_api_issue.json_model["fields"]["summary"]
        search = Search().set_jql(f"reporter = currentUser() and summary ~  '{summary}'").post()
        assert search.status_code == 200, "Status code should be correct"
        assert search.response["total"] == 1, "Number of found issues should be 1"


    def test_search_no_such_issue(self):
        search = Search().set_jql("reporter = currentUser() and status = Canceled").post()
        assert search.status_code == 200, "Status code should be correct"
        assert search.response["total"] == 0, "Number of found issues should be 0"
