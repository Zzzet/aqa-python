import allure

from src.util.driver_container import DriverContainer


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


def pytest_exception_interact(node, call, report):
    allure.attach(DriverContainer().get_driver(DriverContainer).get_screenshot_as_png(),
                  "screenshot",
                  allure.attachment_type.PNG)
