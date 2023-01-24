import pytest
import sys
from base_object.base import BaseObject
from base_object.locators import AbusePageLocators



class AbusePage(BaseObject):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    def get_link(self, link):
        self.open_link(link)


    def count_find_elements(self):

        print('start')
        elems = self.find_product_names(locator=AbusePageLocators.AROMA_BLOCK)
        for element in elems:
            aroma_name = self.find_product_price(element, 'h2')
            for name in aroma_name:
                print(f'\n{name.text}')
                aroma_price = self.find_product_price(element, 'li')
                for price in aroma_price:
                    v = price.text[0] + price.text[1] + price.text[2]
                    if v == '500':
                        print(f'{price.text}')



        print('end')



