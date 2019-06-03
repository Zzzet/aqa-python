import pytest
from requests.auth import HTTPBasicAuth

from src.rest.jira.issue import Issue
from src.rest.jira_resource import JiraResource
from src.util.string_utils import randomString


class ApiBaseTest:
    name = None
    password = None
    basic = None

    @pytest.fixture(scope="function", autouse=True)
    def api_default_login(self, request):
        ApiBaseTest.name = request.config.getoption("name")
        ApiBaseTest.password = request.config.getoption("password")
        ApiBaseTest.basic = HTTPBasicAuth(self.name, self.password)
        JiraResource.set_basic_auth(JiraResource, self.basic)

    @pytest.fixture
    def create_api_issue(self):
        issue_summary = "My_issue_" + randomString()
        issue = Issue() \
            .set_issue_type("Bug") \
            .set_project("WEBINAR") \
            .set_summary(issue_summary) \
            .set_description("blah") \
            .set_priority("Low") \
            .post()
        return issue