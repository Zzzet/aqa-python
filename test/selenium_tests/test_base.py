import pytest
from src.util.driver_container import DriverContainer


class BaseTest:
    driver = None

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, request):
        print("  SETUP")
        base_url = request.config.getoption("--url")
        DriverContainer().create_driver(DriverContainer, base_url)
        yield
        print("  TEARDOWN ")
