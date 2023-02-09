import pytest
from sendtelegram.telegram import send_telegram
import time
from support.logger import log_method
import logging as log
from base_object.base import BaseObject
from base_object.locators import AbusePageLocators

...
names_list = {}


def dict_compare(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    shared_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {o: (d1[o], d2[o]) for o in shared_keys if d1[o] != d2[o]}
    same = set(o for o in shared_keys if d1[o] == d2[o])
    return added, removed, modified, same


class AbusePage(BaseObject):
    log = log_method(logLevel=log.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login(self):
        self.open_link('shop.perfumersapprentice.com/')
        self.click(AbusePageLocators.LOGIN_LINK)
        self.fill_input(AbusePageLocators.EMAIL_FIELD, "Admkaren15@gmail.com")
        self.fill_input(AbusePageLocators.PASSWORD_FIELD, 623914148)
        self.click(AbusePageLocators.LOGIN_BTN)
        time.sleep(5)

    def count_find_elements(self):

        global names_list, data, aroma_name

        self.open_link(f'shop.perfumersapprentice.com/c-84-bulk-sizes.aspx?pagenum={3}')
        spisok = []
        aroma_blocks = self.find_product_names(locator=AbusePageLocators.AROMA_BLOCK)

        for block in aroma_blocks:
            aroma_names = self.find_elems_in_elem(block, 'h2')
            for names in aroma_names:
                aroma_name = names.text
                self.log.info(f"aroma name = {aroma_name}")
                aroma_prices = self.find_elems_in_elem(block, 'li')
                spisok = []

                for price in aroma_prices:

                    prefix = price.text[0:4]

                    if 'gall' in prefix:
                        spisok.append(price.text)

                    elif prefix == 'case':
                        spisok.append(price.text)

                    elif prefix == 'doub':
                        spisok.append(price.text)
                    if len(spisok) > 0:
                        self.log.info(f'FOR {aroma_name} added value : {spisok}')

                if len(spisok) > 0:
                    names_list.update({aroma_name: spisok})


            self.log.info('-----------------------')
            self.log.info(names_list)





    def compare_dicts(self):
        global names_list, data
        print(names_list)
        added, removed, modified, same = dict_compare(names_list, data)
        for products, prises_list in modified.items():
            arr = prises_list[0]
            arr2 = prises_list[1]
            i = 0
            if len(arr) == len(arr2):
                while i < len(arr):
                    if arr[i] != arr2[i]:
                        print(f" {products} \nOLD  {arr[i]} \nNEW {arr2[i]}")

                        i += 1
                    else:
                        i += 1
            else:
                print(f'New position was added/removed \n\nOld file:\n{products}  {arr} '
                      f'\n\nNew file: \n{products}  {arr2}')

            for key, value in names_list.items():
                print(key)
                print(value)
