import allure
from selenium.webdriver.common.by import By

from src.sel.elements.base_element import BaseElement


class BasePage:

    @allure.step
    def backdrop_dissapears(self):
        BaseElement((By.CSS_SELECTOR, "[class='aui-blanket']")).wait_until_not_visible()

    @allure.step
    def details_loaded(self):
        BaseElement((By.CSS_SELECTOR, "[class='details-layout'] > [class='loading']")).wait_until_not_visible()

    @allure.step
    def get_aui_error(self) -> str:
        return BaseElement((By.CSS_SELECTOR, "[class*='aui-message-error']")).get_value()

    @allure.step
    def get_error(self) -> str:
        return BaseElement((By.CSS_SELECTOR, "[class='error']")).get_value()
