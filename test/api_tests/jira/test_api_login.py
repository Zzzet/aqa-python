import pytest
import requests
from requests.auth import HTTPBasicAuth

from src.rest.jira.issue import Issue
from test.api_tests.test_api_base import ApiBaseTest


class TestApiLogin(ApiBaseTest):

    @pytest.mark.parametrize("name, password, response", [("DmytroKarpenko", "DmytroKarpenko", 200),
                                                          ("wrong", "DmytroKarpenko", 401),
                                                          ("DmytroKarpenko", "wrong", 401)])
    def test_login_param(self, create_api_issue: Issue, name, password, response):
        issue = Issue()
        issue.auth = HTTPBasicAuth(name, password)
        issue.key = create_api_issue.key
        issue.get()
        assert issue.status_code == response, "Status code doesn't match"
