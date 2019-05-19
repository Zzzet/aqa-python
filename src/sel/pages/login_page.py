from selenium.webdriver.common.by import By

from src.sel.pages.base_page import BasePage
from src.sel.elements.base_element import BaseElement
from src.util.driver_container import DriverContainer


class LoginPage(BasePage):

    def __init__(self):
        self.driver = DriverContainer().get_driver(DriverContainer)

    def open(self):
        self.driver.get(DriverContainer.base_url)
        return self

    def enter_username(self, username):
        BaseElement((By.ID, "login-form-username")).wait_until_ready().send_keys(username)
        return self

    def enter_password(self, password):
        BaseElement((By.ID, "login-form-password")).wait_until_ready().send_keys(password)
        return self

    def click_login(self):
        BaseElement((By.ID, "login")).wait_until_visible().click()
        return self

    def login_as(self, user, password):
        self.enter_username(user)
        self.enter_password(password)
        self.click_login()
        BaseElement((By.ID, "login")).wait_until_not_visible()
