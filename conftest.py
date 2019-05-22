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
    parser.addoption(
        "--name",
        action="store",
        default="DmytroKarpenko"
    )
    parser.addoption(
        "--password",
        action="store",
        default="DmytroKarpenko"
    )




