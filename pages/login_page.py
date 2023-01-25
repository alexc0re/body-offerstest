import itertools
import time
from support.logger import log_method
import logging as log
import pytest
import sys
import csv
from base_object.base import BaseObject
from base_object.locators import AbusePageLocators



class AbusePage(BaseObject):
    log = log_method(logLevel=log.INFO)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    def get_link(self, link):
        self.open_link(link)

    def login(self):
        self.click(AbusePageLocators.LOGIN_LINK)
        self.fill_input(AbusePageLocators.EMAIL_FIELD, "Admkaren15@gmail.com")
        self.fill_input(AbusePageLocators.PASSWORD_FIELD, 623914148)
        self.click(AbusePageLocators.LOGIN_BTN)
        time.sleep(5)
        self.open_link('shop.perfumersapprentice.com/c-84-bulk-sizes.aspx')



    def count_find_elements(self):
        with open('file.csv', 'w') as f:
            fields = ['Name', 'Price1', 'Price2', 'Price3']
            write = csv.writer(f)
            write.writerow(fields)
            names_list = {}
            all_arr = []
            spisok = []
            print('start')
            elems = self.find_product_names(locator=AbusePageLocators.AROMA_BLOCK)

            for element in elems:

                aroma_names = self.find_product_price(element, 'h2')

                for name in aroma_names:
                    name_list = [name.text, '']
                    all_arr.append(name_list)
                    aromas_prices = self.find_product_price(element, 'li')
                    spisok.clear()


                    for price in aromas_prices:

                        text = price.text
                        prefix = text[0] + text[1] + text[2] + text[3]

                        if prefix == 'gall' or prefix == 'case' or prefix == 'doub':
                            spisok.append(price.text)
                    all_arr.append(spisok)

            print(all_arr)
            write.writerows(all_arr)

            # i = 0
            # for key in all_arr:
            #     rows = [key]
            #     # using csv.writer method from CSV package
            #     write.writerows(rows)

    def compare_lists(self):
        with open('prices.csv', 'r') as csv_1:
            with open('file.csv', 'r') as csv_2:
                reader1 = csv.reader(csv_1, delimiter=',')
                reader2 = csv.reader(csv_2, delimiter=',')
                try:
                    i_line = 0
                    while True:
                        row_1 = next(reader1)
                        row_2 = next(reader2)
                        i_line += 1
                        if row_1 != row_2:
                            for k, item in enumerate(row_1):
                                if item != row_2[k]:
                                    print(f"difference Line {i_line}: ")
                                    print(f"New price {row_1[k-1]}: {row_1[k]}")
                                    print(f"Old price {row_2[k-1]}: {row_2[k]}")
                except StopIteration:
                    print("line numbers differ!")
                finally:
                    print(f"lines parsed = {i_line}")


    print('end')



