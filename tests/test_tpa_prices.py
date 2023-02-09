import time
from base_object.locators import AbusePageLocators
import pytest




def test_find_prices(abuse_page):
    abuse_page.login()
    abuse_page.count_find_elements()
    abuse_page.count_find_elements2()
    abuse_page.count_find_elements3()
    abuse_page.compare_dicts()


