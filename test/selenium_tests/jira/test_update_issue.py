import pytest

from src.sel.pages.create_issue_page import CreateIssuePage
from src.sel.pages.home_page import HomePage
from src.sel.pages.issue_details_page import IssuePage
from src.util.string_utils import randomString

from src.sel.pages.login_page import LoginPage
from test.selenium_tests.test_base import BaseTest
from src.sel.pages.header import Header


@pytest.mark.usefixtures("default_login")
class TestCreateIssues(BaseTest):

    def test_update_summary(self, create_issue):
        IssuePage().click_edit_btn()
        CreateIssuePage() \
            .set_summary("upd") \
            .click_submit_btn()

    def test_update_priority(self, create_issue):
        IssuePage().click_edit_btn()
        CreateIssuePage() \
            .set_priority("Low") \
            .click_submit_btn()

    def test_update_assignee(self, create_issue):
        IssuePage().click_edit_btn()
        CreateIssuePage() \
            .set_assignee("Andrew Pospelko") \
            .click_submit_btn()

    @pytest.fixture
    def create_issue(self):
        Header().click_create_btn()

        CreateIssuePage().set_project("Webinar") \
            .set_issue_type("Story") \
            .set_summary("My issue") \
            .click_submit_btn()

        HomePage().notification.open_issue()
