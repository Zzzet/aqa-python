import pytest

from sel.pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption(
        "-H",
        action="store",
        default="localhost"
    )

    parser.addoption(
        "-P",
        action="store",
        default="4444"
    )


@pytest.fixture()
def default_login():
    LoginPage().open() \
        .enter_username("DmytroKarpenko") \
        .enter_password("DmytroKarpenko") \
        .click_login()
