import pytest

from src.sel.pages.create_issue_page import CreateIssuePopup
from src.sel.pages.issue_details_page import IssuePage
from test.selenium_tests.test_base import BaseTest


@pytest.mark.usefixtures("default_login")
class TestCreateIssues(BaseTest):

    def test_update_summary(self, create_issue):
        IssuePage().click_edit_btn()
        CreateIssuePopup() \
            .set_summary("upd") \
            .click_update_btn()
        summary = IssuePage().get_summary()
        assert summary.__contains__("upd")

    def test_update_priority(self, create_issue):
        IssuePage().click_edit_btn()
        CreateIssuePopup() \
            .set_priority("Low") \
            .click_update_btn()
        priority = IssuePage().get_priority()
        assert priority.__contains__("Low")

    def test_update_assignee(self, create_issue):
        IssuePage().click_edit_btn()
        CreateIssuePopup() \
            .set_assignee("DmytroKarpenko") \
            .click_update_btn()
        assignee = IssuePage().get_assignee()
        assert assignee.__contains__("DmytroKarpenko")
