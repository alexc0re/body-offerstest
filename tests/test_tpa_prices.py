import time
from base_object.locators import AbusePageLocators
import pytest




def test_find_prices(abuse_page):
    abuse_page.get_link('shop.perfumersapprentice.com/c-84-bulk-sizes.aspx')
    abuse_page.login()
    abuse_page.count_find_elements()


