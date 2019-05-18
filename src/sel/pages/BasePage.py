from selenium.webdriver.common.by import By

from src.sel.elements.base_element import BaseElement


class BasePage:
    def backdrop_dissapears(self):
        BaseElement((By.CSS_SELECTOR, "[class='aui-blanket']")).wait_until_not_visible()
