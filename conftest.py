import pytest

from sel.pages.login_page import LoginPage


@pytest.fixture()
def default_login():
    LoginPage().open() \
        .enter_username("DmytroKarpenko") \
        .enter_password("DmytroKarpenko") \
        .click_login()
