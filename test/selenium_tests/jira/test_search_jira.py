import pytest

from sel.pages.home_page import HomePage
from selenium_tests.test_base import BaseTest


@pytest.mark.usefixtures("default_login")
class TestJira(BaseTest):

    def test_search(self):
        HomePage().header.open_search()
        pass

    # no such issue reporter = DmytroKarpenko and status = Resolved

    # 5 issues reporter = currentUser() and summary ~  "upd-123"

    # 1 issue reporter = currentUser() and summary ~  "upd-123"
