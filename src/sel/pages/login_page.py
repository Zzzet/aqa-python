import allure
from selenium.webdriver.common.by import By

from src.sel.pages.base_page import BasePage
from src.sel.elements.base_element import BaseElement
from src.util.driver_container import DriverContainer


class LoginPage(BasePage):

    login_btn = (By.ID, "login")

    def __init__(self):
        BaseElement(self.login_btn).wait_until_visible()
        self.driver = DriverContainer().get_driver(DriverContainer)

    @allure.step
    def open(self):
        self.driver.get(DriverContainer.base_url)
        return self

    @allure.step
    def enter_username(self, username):
        BaseElement((By.ID, "login-form-username")).send(username)
        return self

    @allure.step
    def enter_password(self, password):
        BaseElement((By.ID, "login-form-password")).send(password)
        return self

    @allure.step
    def click_login(self):
        BaseElement(self.login_btn).click()
        return self

    @allure.step
    def login_as(self, user, password):
        self.enter_username(user)
        self.enter_password(password)
        self.click_login()
        BaseElement(self.login_btn).wait_until_not_visible()
