import pytest

from src.sel.pages.create_issue_page import CreateIssuePopup
from src.sel.pages.home_page import HomePage
from src.sel.pages.login_page import LoginPage
from src.util.driver_container import DriverContainer


class BaseTest:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, request):
        print("  SETUP")
        base_url = request.config.getoption("--url")
        DriverContainer().create_driver(DriverContainer, base_url)
        yield
        print("  TEARDOWN ")
        DriverContainer.close_driver(DriverContainer)

    @pytest.fixture(scope="function", autouse=True)
    def get_def_user(self, request):
        self.name = request.config.getoption("name")
        self.password = request.config.getoption("password")


    @pytest.fixture
    def create_issue(self):
        HomePage().header.click_create_btn()

        CreateIssuePopup().set_project("Webinar") \
            .set_issue_type("Story") \
            .set_summary("My issue") \
            .click_submit_btn()

        HomePage().notification.open_issue()

    @pytest.fixture()
    def default_login(self):
        LoginPage().open() \
            .login_as(self.name, self.password)
