import allure
import logging

from src.util.driver_container import DriverContainer

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s %(name)-4s %(levelname)-4s %(message)s', datefmt='%H:%M:%S')

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)



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
    driver = DriverContainer().get_driver(DriverContainer)
    if driver is not None:
        allure.attach(driver.get_screenshot_as_png(),
                      "screenshot",
                      allure.attachment_type.PNG)
