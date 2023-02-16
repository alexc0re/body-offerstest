import time
from base_object.locators import AbusePageLocators
import pytest




def test_find_prices(abuse_page):
    abuse_page.login()
    abuse_page.count_find_elements()


