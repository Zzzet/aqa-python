import pytest

from src.sel.pages.create_issue_page import CreateIssuePage
from src.sel.pages.issue_details_page import IssuePage
from test.selenium_tests.test_base import BaseTest


@pytest.mark.usefixtures("default_login")
class TestCreateIssues(BaseTest):

    def test_update_summary(self, create_issue):
        IssuePage().click_edit_btn()
        CreateIssuePage() \
            .set_summary("upd") \
            .click_update_btn()

    def test_update_priority(self, create_issue):
        IssuePage().click_edit_btn()
        CreateIssuePage() \
            .set_priority("Low") \
            .click_update_btn()

    def test_update_assignee(self, create_issue):
        IssuePage().click_edit_btn()
        CreateIssuePage() \
            .set_assignee("Artur Piluck") \
            .click_update_btn()
