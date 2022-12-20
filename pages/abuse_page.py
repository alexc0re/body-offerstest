import pytest

from base_object.base import BaseObject
from base_object.locators import AbusePageLocators
from links.linksList import test_links

class AbusePage(BaseObject):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def goto_page(self,link):
        self.open_link(link)


    def find_cf_abuse(self):
        try:
            self.is_visible(AbusePageLocators.ABUSE)
        except:
            pass
