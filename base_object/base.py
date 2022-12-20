import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from links.linksList import test_links



class BaseObject:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open_link(self, link):
        self.driver.get(f'http://{link}')


    def is_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

