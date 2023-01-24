import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait




class BaseObject:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)


    def open_link(self, link):
        self.driver.get(f'http://{link}')


    def is_visible_elem(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))


    def find_product_names(self, locator):
        # return self.wait.until(ec.visibility_of_all_elements_located(locator))
        return self.wait.until(ec.presence_of_all_elements_located(locator))

    def find_product_price(self, element, locator):
        return element.find_elements_by_css_selector(locator)


    def find_element(self, locator):
        self.find_element(locator)

