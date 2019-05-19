import pytest

from sel.pages.login_page import LoginPage


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
