import pytest
from src.sel.pages.home_page import HomePage
from src.sel.pages.login_page import LoginPage
from src.sel.pages.create_issue_page import CreateIssuePage


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://jira.hillel.it/"
    )


@pytest.fixture()
def default_login():
    LoginPage().open() \
        .login_as("DmytroKarpenko", "DmytroKarpenko")


@pytest.fixture
def create_issue():
    HomePage().header.click_create_btn()

    CreateIssuePage().set_project("Webinar") \
        .set_issue_type("Story") \
        .set_summary("My issue") \
        .click_submit_btn()

    HomePage().notification.open_issue()
