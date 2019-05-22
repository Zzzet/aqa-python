from selenium.webdriver.common.by import By

from src.sel.pages.base_page import BasePage
from src.sel.elements.base_element import BaseElement
from src.util.driver_container import DriverContainer


class LoginPage(BasePage):

    login_btn = (By.ID, "login")

    def __init__(self):
        self.driver = DriverContainer().get_driver(DriverContainer)

    def open(self):
        self.driver.get(DriverContainer.base_url)
        return self

    def enter_username(self, username):
        BaseElement((By.ID, "login-form-username")).set_value(username)
        return self

    def enter_password(self, password):
        BaseElement((By.ID, "login-form-password")).set_value(password)
        return self

    def click_login(self):
        BaseElement(self.login_btn).click()
        return self

    def login_as(self, user, password):
        self.enter_username(user)
        self.enter_password(password)
        self.click_login()
        BaseElement(self.login_btn).wait_until_not_visible()
