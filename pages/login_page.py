
from sendtelegram.telegram import send_telegram
import time
from support.logger import log_method
import logging as log
import deepdiff
import csv
from base_object.base import BaseObject
from base_object.locators import AbusePageLocators

data = {'ABSINTHE FLAVOR **': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'ABSINTHE FLAVOR CONCENTRATE': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'ABSINTHE II FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'ACAI FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'ACETYL PYRAZINE 5 PG': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'ALMOND AMARETTO FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'ALMOND FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'APPLE (TART GRANNY SMITH) FLAVOR **': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'APPLE (TART GREEN APPLE) FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'APPLE CANDY FLAVOR**': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'APPLE FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'APPLE PIE FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'APRICOT FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BANANA CREAM FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BANANA FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BANANA NUT BREAD FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BANANAS FOSTER FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BAVARIAN CREAM FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BERRY CEREAL FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BERRY MIX FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BERRY TOBACCO TYPE FLAVOR CC': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BIRCH BEER AND TOBACCO TYPE FLAVOR CC': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BITTER NUT EXTRA FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BITTERSWEET CHOCOLATE FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BLACK CHERRY FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BLACK CURRANT FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BLACK HONEY FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BLACK TEA DELUXE FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BLACK TEA FLAVOR**': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BLACKBERRY FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BLUE RASPBERRY FLAVOR **': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BLUEBERRY (RIPE) FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BLUEBERRY (WILD) FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BLUEBERRY CANDY FLAVOR (PG)': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BLUEBERRY CANDY FLAVOR (TRIACETIN)': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BLUEBERRY FLAVOR (EXTRA)': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BOURBON FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BOYSENBERRY DELUXE FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BOYSENBERRY FLAVOR **': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BRANDY FLAVOR **': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BROWN SUGAR FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BUBBLEGUM (FRUITY) FLAVOR **': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BUBBLEGUM FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BUTTER FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BUTTERSCOTCH FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'BUTTERSCOTCH II FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CANNABIS TYPE FLAVOR**': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CANTALOUPE FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CAPPUCCINO FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CARAMEL (ORIGINAL) FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CARAMEL CANDY FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CARAMEL CAPPUCCINO FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CARAMEL FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CC SAMPLE PACK - MINT': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CC SAMPLE PACK - TOBACCO': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CHAI TEA FLAVOR **': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CHAI TEA II FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CHAMPAGNE TYPE FLAVOR (PG)': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CHEESECAKE FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CHEESECAKE FLAVOR (GRAHAM CRUST)': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CHERRY BLOSSOM (PG)': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CHERRY EXTRACT FLAVOR**': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CHILI MANGO FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CHOCOLATE COCONUT ALMOND CANDY BAR FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CHOCOLATE FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CIGARILLO FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CINNAMON DANISH FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CINNAMON FLAVOR **': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CINNAMON RED HOT (PG)': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CINNAMON RED HOT FLAVOR**': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CINNAMON SPICE FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CINNAMON SUGAR COOKIE': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CITRUS PUNCH FLAVOR **': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CITRUS PUNCH II FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CLOVE FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'COCOA ROUNDS FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'COCOA TOBACCO TYPE FLAVOR CC': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'COCONUT CANDY FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'COCONUT EXTRA FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'COCONUT FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'COFFEE (KONA) FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'COFFEE FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'COLA CHERRY FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'COLA FIZZ FLAVOR**': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'COLA FLAVOR**': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CARDAMOM FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'COLA SODA FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'COLA SYRUP FLAVOR**': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'COTTON CANDY (CIRCUS)': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'COTTON CANDY FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CRANBERRY FLAVOR**': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CRANBERRY SAUCE FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CREAM SODA FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CREME DE MENTHE FLAVOR **': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CREME DE MENTHE II FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CRUNCHY CEREAL FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CUBANO TYPE FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CUCUMBER DELUXE FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'CUCUMBER FLAVOR **': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'DAIRY/MILK FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'DARK RUM FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'DATE FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'DK TOBACCO BASE FLAVOR **': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'DK TOBACCO II FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'DOUBLE CHOCOLATE (CLEAR) FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'DOUBLE CHOCOLATE (DARK) FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'DR. POP FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'DRAGONFRUIT FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'DULCE DE LECHE CARAMEL FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'DULCE DE LECHE FLAVOR **': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'DX BANANA CREAM': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'DX BANANAS FOSTER FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'DX BAVARIAN CREAM': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'DX BROWN SUGAR FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'DX BUTTERSCOTCH FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'DX CARAMEL ORIGINAL': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'DX CINNAMON DANISH': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'DX COCONUT CANDY FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'DX COCONUT FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)'], 'DX FROSTED DONUT FLAVOR': ['gallon - $100.00 (USD)', 'case (4)  - $375.00 (USD)', 'double case (8)  - $742.00 (USD)']}



names_list = {}



def dict_compare(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    shared_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {o : (d1[o], d2[o]) for o in shared_keys if d1[o] != d2[o]}
    same = set(o for o in shared_keys if d1[o] == d2[o])
    return added, removed, modified, same




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
        global names_list, data
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

                        if prefix == 'gall' :
                            spisok.append(price.text)
                        elif prefix == 'case' :
                            spisok.append(text.replace('2week lead time', ''))
                        elif  prefix == 'doub':
                            spisok.append(text.replace('2 week lead time', ''))
                    names_list.update({str(name.text): spisok})
                    added, removed, modified, same = dict_compare(names_list, data)
                    diff = deepdiff.DeepDiff(names_list, data)

        for products, prises_list in modified.items():
            arr = prises_list[0]
            arr2 = prises_list[1]
            i = 0
            if len(arr) == len(arr2):
                while i < len(arr):
                    if arr[i] != arr2[i]:
                        send_telegram(f" {products} \nOLD  {arr[i]} \nNEW {arr2[i]}")
                        i+=1
                    else:
                        i += 1
            else:
                send_telegram(f'New position was added/removed \n\nOld file:\n{products}  {arr} '
                              f'\n\nNew file: \n{products}  {arr2}')


        print(names_list)



