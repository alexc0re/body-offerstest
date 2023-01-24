import time
from base_object.locators import AbusePageLocators
import pytest




def test_find_prices(abuse_page):
    abuse_page.get_link('shop.perfumersapprentice.com/c-51-aroma-molecules-a-e.aspx')
    abuse_page.count_find_elements()
