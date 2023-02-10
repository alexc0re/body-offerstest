import pytest
from sendtelegram.telegram import send_telegram
import time
from support.logger import log_method
import logging as log
from base_object.base import BaseObject
from base_object.locators import AbusePageLocators

...
names_list = {}
data = {
    "ABSINTHE FLAVOR **": [
        "gallon - $11.70 (USD)",
        "case (4) 2week lead time - $460.00 (USD)",
    ],
    "ABSINTHE II FLAVOR": [
        "gallon - $133.80 (USD)",
        "case (4) 2week lead time - $528.00 (USD)",
    ],
    "ACAI FLAVOR": [
        "gallon - $110.00 (USD)",
        "case (4) 2week lead time - $420.00 (USD)",
        "double case (8) 2 week lead time - $824.00 (USD)",
    ],
    "ACETYL PYRAZINE 5 PG": [
        "gallon - $220.00 (USD)",
        "case (4 gallons) - $800.00 (USD)",
        "double case (8) 2 week lead time - $1,560.00 (USD)",
    ],
    "ALMOND AMARETTO FLAVOR": [
        "gallon - $90.00 (USD)",
        "case (4) 2week lead time - $320.00 (USD)",
    ],
    "ALMOND FLAVOR": ["gallon - $85.50 (USD)"],
    "APPLE (TART GRANNY SMITH) FLAVOR **": [
        "gallon - $114.00 (USD)",
        "case (4) 2week lead time - $416.00 (USD)",
    ],
    "APPLE (TART GREEN APPLE) FLAVOR": [
        "gallon - $135.00 (USD)",
        "case (4) 2week lead time - $520.00 (USD)",
        "double case (8) 2 week lead time - $1,024.00 (USD)",
    ],
    "APPLE CANDY FLAVOR**": [
        "gallon - $114.00 (USD)",
        "case (4 gallons) - $416.00 (USD)",
        "double case (8) 2 week lead time - $808.24 (USD)",
    ],
    "APPLE FLAVOR": [
        "gallon - $102.60 (USD)",
        "case (4 gallons) - $360.00 (USD)",
        "double case (8) 2 week lead time - $679.78 (USD)",
    ],
    "APPLE PIE FLAVOR": [
        "gallon - $114.00 (USD)",
        "case (4 gallons) - $420.00 (USD)",
        "double case (8) 2 week lead time - $768.24 (USD)",
    ],
    "APRICOT FLAVOR": ["gallon - $96.90 (USD)", "case (4 gallons) - $360.00 (USD)"],
    "BANANA CREAM FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4 gallons) - $336.00 (USD)",
        "double case (8) 2 week lead time - $660.00 (USD)",
    ],
    "BANANA FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $320.00 (USD)",
        "double case (8) 2 week lead time - $624.00 (USD)",
    ],
    "BANANA NUT BREAD FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4 gallons) - $334.00 (USD)",
        "double case (8) 2 week lead time - $652.00 (USD)",
    ],
    "BANANAS FOSTER FLAVOR": [
        "gallon - $127.00 (USD)",
        "case (4) 2week lead time - $500.00 (USD)",
        "double case (8) 2 week lead time - $992.00 (USD)",
    ],
    "BAVARIAN CREAM FLAVOR": [
        "gallon - $99.75 (USD)",
        "case (4 gallons) - $392.00 (USD)",
        "double case (8) - $774.00 (USD)",
    ],
    "BERRY CEREAL FLAVOR": [
        "gallon - $120.00 (USD)",
        "case (4 gallons) - $472.00 (USD)",
        "double case (8) 2 week lead time - $928.00 (USD)",
    ],
    "BERRY MIX FLAVOR": [
        "gallon - $114.00 (USD)",
        "case (4) 2week lead time - $448.00 (USD)",
        "double case (8) 2 week lead time - $880.00 (USD)",
    ],
    "BERRY TOBACCO TYPE FLAVOR CC": ["gallon - $240.00 (USD)"],
    "BIRCH BEER AND TOBACCO TYPE FLAVOR CC": ["gallon - $260.00 (USD)"],
    "BITTER NUT EXTRA FLAVOR": [
        "gallon - $240.00 (USD)",
        "case (4) 2week lead time - $928.00 (USD)",
    ],
    "BITTERSWEET CHOCOLATE FLAVOR": ["gallon - $148.20 (USD)"],
    "BLACK CHERRY FLAVOR": [
        "gallon - $91.20 (USD)",
        "case (4 gallons) - $320.00 (USD)",
        "double case (8) 2 week lead time - $624.00 (USD)",
    ],
    "BLACK CURRANT FLAVOR": [
        "gallon - $96.00 (USD)",
        "case (4 gallons) - $376.00 (USD)",
        "double case (8) 2 week lead time - $736.00 (USD)",
    ],
    "BLACK HONEY FLAVOR": [
        "gallon - $116.00 (USD)",
        "case (4) 2week lead time - $424.00 (USD)",
        "double case (8) 2 week lead time - $800.00 (USD)",
    ],
    "BLACKBERRY FLAVOR": [
        "gallon - $91.20 (USD)",
        "case (4 gallons) - $356.80 (USD)",
        "double case (8) 2 week lead time - $697.60 (USD)",
    ],
    "BLUE RASPBERRY FLAVOR **": [
        "gallon - $226.00 (USD)",
        "case (4) 2week lead time - $896.00 (USD)",
    ],
    "BLUEBERRY (RIPE) FLAVOR": ["case (4) 2week lead time - $635.00 (USD)"],
    "BLUEBERRY (WILD) FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4 gallons) - $332.00 (USD)",
        "double case (8) 2 week lead time - $648.00 (USD)",
    ],
    "BLUEBERRY CANDY FLAVOR (PG)": [
        "gallon - $148.20 (USD)",
        "case (4 gallons) - $552.80 (USD)",
        "double case (8) 2 week lead time - $1,099.00 (USD)",
    ],
    "BLUEBERRY CANDY FLAVOR (TRIACETIN)": ["gallon - $148.20 (USD)"],
    "BLUEBERRY FLAVOR (EXTRA)": [
        "gallon - $85.50 (USD)",
        "case (4 gallons) - $332.00 (USD)",
        "double case (8) 2 week lead time - $648.00 (USD)",
    ],
    "BOURBON FLAVOR": [
        "gallon - $127.50 (USD)",
        "case (4) 2week lead time - $504.00 (USD)",
    ],
    "BOYSENBERRY DELUXE FLAVOR": ["gallon - $148.00 (USD)"],
    "BOYSENBERRY FLAVOR **": ["gallon - $148.00 (USD)"],
    "BRANDY FLAVOR **": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $336.00 (USD)",
    ],
    "BROWN SUGAR FLAVOR": [
        "gallon - $116.85 (USD)",
        "case (4 gallons) - $427.40 (USD)",
        "double case (8) 2 week lead time - $812.00 (USD)",
    ],
    "BUBBLEGUM (FRUITY) FLAVOR **": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $332.00 (USD)",
        "double case (8) 2 week lead time - $648.00 (USD)",
    ],
    "BUBBLEGUM FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4 gallons) - $334.00 (USD)",
        "double case (8) 2 week lead time - $652.00 (USD)",
    ],
    "BUTTER FLAVOR": [
        "gallon - $119.70 (USD)",
        "case (4 gallons) - $438.80 (USD)",
        "double case (8) 2 week lead time - $864.00 (USD)",
    ],
    "BUTTERSCOTCH FLAVOR": [
        "gallon - $114.00 (USD)",
        "case (4 gallons) - $444.00 (USD)",
        "double case (8) 2 week lead time - $872.00 (USD)",
    ],
    "BUTTERSCOTCH II FLAVOR": ["gallon - $114.00 (USD)"],
    "CANNABIS TYPE FLAVOR**": [
        "gallon - $114.00 (USD)",
        "case (4) 2week lead time - $416.00 (USD)",
    ],
    "CANTALOUPE FLAVOR": [
        "gallon - $120.00 (USD)",
        "case (4 gallons) - $472.00 (USD)",
        "double case (8) 2 week lead time - $928.00 (USD)",
    ],
    "CAPPUCCINO FLAVOR": [
        "gallon - $91.20 (USD)",
        "case (4) 2week lead time - $352.00 (USD)",
    ],
    "CARAMEL (ORIGINAL) FLAVOR": [
        "gallon - $91.20 (USD)",
        "case (4) 2week lead time - $356.80 (USD)",
        "double case (8) 2 week lead time - $697.60 (USD)",
    ],
    "CARAMEL CANDY FLAVOR": [
        "gallon - $95.00 (USD)",
        "case (4 gallons) - $368.00 (USD)",
        "double case (8) 2 week lead time - $720.00 (USD)",
    ],
    "CARAMEL CAPPUCCINO FLAVOR": [
        "gallon - $210.00 (USD)",
        "case (4) 2week lead time - $800.00 (USD)",
    ],
    "CARAMEL FLAVOR": [
        "gallon - $91.20 (USD)",
        "case (4) 2week lead time - $356.00 (USD)",
        "double case (8) 2 week lead time - $696.00 (USD)",
    ],
    "CHAI TEA FLAVOR **": [
        "gallon - $115.00 (USD)",
        "case (4) 2week lead time - $420.00 (USD)",
        "double case (8) 2 week lead time - $824.00 (USD)",
    ],
    "CHAI TEA II FLAVOR": [
        "gallon - $115.00 (USD)",
        "case (4) 2week lead time - $420.00 (USD)",
    ],
    "CHAMPAGNE TYPE FLAVOR (PG)": [
        "gallon - $85.00 (USD)",
        "case (4) 2week lead time - $328.00 (USD)",
        "double case (8) 2 week lead time - $640.00 (USD)",
    ],
    "CHEESECAKE FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $302.00 (USD)",
        "double case (8) 2 week lead time - $550.00 (USD)",
    ],
    "CHEESECAKE FLAVOR (GRAHAM CRUST)": [
        "gallon - $105.00 (USD)",
        "case (4) 2week lead time - $412.00 (USD)",
        "double case (8) 2 week lead time - $808.00 (USD)",
    ],
    "CHERRY BLOSSOM (PG)": [
        "gallon - $148.20 (USD)",
        "case (4) 2week lead time - $480.00 (USD)",
    ],
    "CHERRY EXTRACT FLAVOR**": [
        "gallon - $85.00 (USD)",
        "case (4) 2week lead time - $320.00 (USD)",
        "double case (8) 2 week lead time - $600.00 (USD)",
    ],
    "CHILI MANGO FLAVOR": ["case (4 gallons) - $540.00 (USD)"],
    "CHOCOLATE COCONUT ALMOND CANDY BAR FLAVOR": ["gallon - $122.50 (USD)"],
    "CHOCOLATE FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $302.00 (USD)",
        "double case (8) 2 week lead time - $547.08 (USD)",
    ],
    "CIGARILLO FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $332.00 (USD)",
        "double case (8) 2 week lead time - $656.00 (USD)",
    ],
    "CINNAMON DANISH FLAVOR": [
        "gallon - $105.00 (USD)",
        "case (4) 2week lead time - $380.00 (USD)",
        "double case (8) 2 week lead time - $748.00 (USD)",
    ],
    "CINNAMON FLAVOR **": [
        "gallon - $102.00 (USD)",
        "case (4) 2week lead time - $404.00 (USD)",
    ],
    "CINNAMON RED HOT (PG)": [
        "gallon - $100.00 (USD)",
        "case (4) 2week lead time - $360.00 (USD)",
    ],
    "CINNAMON RED HOT FLAVOR**": [
        "gallon - $100.00 (USD)",
        "case (4 gallons) - $388.00 (USD)",
        "double case (8) 2 week lead time - $752.00 (USD)",
    ],
    "CINNAMON SPICE FLAVOR": [
        "gallon - $110.00 (USD)",
        "case (4) 2week lead time - $400.00 (USD)",
    ],
    "CINNAMON SUGAR COOKIE": [
        "gallon - $92.00 (USD)",
        "case (4) 2week lead time - $360.00 (USD)",
        "double case (8) 2 week lead time - $696.00 (USD)",
    ],
    "CITRUS PUNCH FLAVOR **": [
        "gallon - $85.50 (USD)",
        "case (4 gallons) - $332.00 (USD)",
        "double case (8) 2 week lead time - $648.00 (USD)",
    ],
    "CITRUS PUNCH II FLAVOR": [
        "gallon - $96.90 (USD)",
        "case (4) 2week lead time - $372.00 (USD)",
        "double case (8) 2 week lead time - $728.00 (USD)",
    ],
    "CLOVE FLAVOR": [
        "gallon - $125.00 (USD)",
        "case (4) 2week lead time - $475.00 (USD)",
    ],
    "COCOA ROUNDS FLAVOR": [
        "gallon - $135.00 (USD)",
        "case (4) 2week lead time - $528.00 (USD)",
    ],
    "COCOA TOBACCO TYPE FLAVOR CC": ["gallon - $280.00 (USD)"],
    "COCONUT CANDY FLAVOR": [
        "gallon - $117.00 (USD)",
        "case (4) 2week lead time - $462.00 (USD)",
        "double case (8) 2 week lead time - $912.00 (USD)",
    ],
    "COCONUT EXTRA FLAVOR": [
        "gallon - $148.20 (USD)",
        "case (4) 2week lead time - $552.00 (USD)",
        "double case (8) 2 week lead time - $1,088.00 (USD)",
    ],
    "COCONUT FLAVOR": [
        "gallon - $102.00 (USD)",
        "case (4 gallons) - $400.00 (USD)",
        "double case (8) 2 week lead time - $776.00 (USD)",
    ],
    "COFFEE (KONA) FLAVOR": ["gallon - $115.00 (USD)"],
    "COFFEE FLAVOR": [
        "gallon - $96.90 (USD)",
        "case (4) 2week lead time - $347.60 (USD)",
    ],
    "COLA CHERRY FLAVOR": [
        "gallon - $150.00 (USD)",
        "case (4) 2week lead time - $592.00 (USD)",
    ],
    "COLA FIZZ FLAVOR**": [
        "gallon - $117.00 (USD)",
        "case (4) 2week lead time - $428.00 (USD)",
        "double case (8) 2 week lead time - $791.52 (USD)",
    ],
    "COLA FLAVOR**": [
        "gallon - $117.00 (USD)",
        "case (4) 2week lead time - $428.00 (USD)",
        "double case (8) 2 week lead time - $791.52 (USD)",
    ],
    "CARDAMOM FLAVOR": ["gallon - $105.00 (USD)"],
    "COLA SODA FLAVOR": [
        "gallon - $170.00 (USD)",
        "case (4) 2week lead time - $672.00 (USD)",
    ],
    "COLA SYRUP FLAVOR**": [
        "gallon - $102.00 (USD)",
        "case (4) 2week lead time - $368.00 (USD)",
        "double case (8) 2 week lead time - $720.00 (USD)",
    ],
    "COTTON CANDY (CIRCUS)": [
        "gallon - $119.00 (USD)",
        "case (4) 2week lead time - $468.00 (USD)",
        "double case (8) 2 week lead time - $920.00 (USD)",
    ],
    "COTTON CANDY FLAVOR": [
        "gallon - $84.00 (USD)",
        "case (4 gallons) - $328.00 (USD)",
        "double case (8) 2 week lead time - $640.00 (USD)",
    ],
    "CRANBERRY FLAVOR**": [
        "case (4) 2week lead time - $380.00 (USD)",
        "double case (8) 2 week lead time - $736.00 (USD)",
    ],
    "CRANBERRY SAUCE FLAVOR": [
        "gallon - $133.00 (USD)",
        "case (4) 2week lead time - $524.00 (USD)",
    ],
    "CREAM SODA FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $322.00 (USD)",
        "double case (8) 2 week lead time - $608.00 (USD)",
    ],
    "CREME DE MENTHE FLAVOR **": [
        "gallon - $91.20 (USD)",
        "case (4) 2week lead time - $356.00 (USD)",
        "double case (8) 2 week lead time - $696.00 (USD)",
    ],
    "CREME DE MENTHE II FLAVOR": [
        "gallon - $114.00 (USD)",
        "case (4) 2week lead time - $448.00 (USD)",
        "double case (8) 2 week lead time - $880.00 (USD)",
    ],
    "CRUNCHY CEREAL FLAVOR": [
        "gallon - $114.00 (USD)",
        "case (4) 2week lead time - $416.00 (USD)",
        "double case (8) 2 week lead time - $808.24 (USD)",
    ],
    "CUBANO TYPE FLAVOR": [
        "gallon - $105.00 (USD)",
        "case (4) 2week lead time - $360.00 (USD)",
        "double case (8) 2 week lead time - $712.00 (USD)",
    ],
    "CUCUMBER DELUXE FLAVOR": [
        "gallon - $148.20 (USD)",
        "case (4) 2week lead time - $552.00 (USD)",
    ],
    "CUCUMBER FLAVOR **": [
        "gallon - $114.00 (USD)",
        "case (4) 2week lead time - $440.00 (USD)",
        "double case (8) 2 week lead time - $763.00 (USD)",
    ],
    "DAIRY/MILK FLAVOR": [
        "gallon - $71.25 (USD)",
        "case (4 gallons) - $280.00 (USD)",
        "double case (8) 2 week lead time - $548.00 (USD)",
    ],
    "DARK RUM FLAVOR": [
        "gallon - $135.00 (USD)",
        "case (4) 2week lead time - $528.00 (USD)",
    ],
    "DK TOBACCO BASE FLAVOR **": [
        "gallon - $165.00 (USD)",
        "case (4) 2week lead time - $644.00 (USD)",
        "double case (8) 2 week lead time - $1,276.00 (USD)",
    ],
    "DK TOBACCO II FLAVOR": [
        "gallon - $230.80 (USD)",
        "case (4) 2week lead time - $916.00 (USD)",
        "double case (8) 2 week lead time - $1,816.00 (USD)",
    ],
    "DOUBLE CHOCOLATE (CLEAR) FLAVOR": [
        "gallon - $140.00 (USD)",
        "case (4 gallons) - $520.00 (USD)",
        "double case (8) 2 week lead time - $1,010.00 (USD)",
    ],
    "DOUBLE CHOCOLATE (DARK) FLAVOR": [
        "gallon - $114.00 (USD)",
        "case (4) 2week lead time - $416.00 (USD)",
        "double case (8) 2 week lead time - $816.00 (USD)",
    ],
    "DR. POP FLAVOR": [
        "gallon - $119.00 (USD)",
        "case (4) 2week lead time - $440.50 (USD)",
    ],
    "DRAGONFRUIT FLAVOR": [
        "gallon - $91.20 (USD)",
        "case (4 gallons) - $356.80 (USD)",
        "double case (8) 2 week lead time - $697.60 (USD)",
    ],
    "DULCE DE LECHE CARAMEL FLAVOR": [
        "gallon - $114.00 (USD)",
        "case (4) 2week lead time - $444.00 (USD)",
        "double case (8) 2 week lead time - $872.00 (USD)",
    ],
    "DULCE DE LECHE FLAVOR **": [
        "gallon - $114.00 (USD)",
        "case (4 gallons) - $444.00 (USD)",
        "double case (8) 2 week lead time - $864.00 (USD)",
    ],
    "DX BANANA CREAM": [
        "gallon - $85.50 (USD)",
        "case (4 gallons) - $334.00 (USD)",
        "double case (8) 2 week lead time - $652.00 (USD)",
    ],
    "DX BANANAS FOSTER FLAVOR": [
        "gallon - $120.00 (USD)",
        "case (4) 2week lead time - $450.00 (USD)",
    ],
    "DX BAVARIAN CREAM": [
        "gallon - $99.75 (USD)",
        "case (4 gallons) - $392.00 (USD)",
        "double case (8) 2 week lead time - $768.00 (USD)",
    ],
    "DX BROWN SUGAR FLAVOR": [
        "gallon - $147.25 (USD)",
        "case (4) 2week lead time - $584.00 (USD)",
    ],
    "DX BUTTERSCOTCH FLAVOR": [
        "gallon - $119.70 (USD)",
        "case (4) 2week lead time - $438.80 (USD)",
    ],
    "DX CARAMEL ORIGINAL": [
        "gallon - $91.20 (USD)",
        "case (4 gallons) - $324.80 (USD)",
        "double case (8) 2 week lead time - $609.60 (USD)",
    ],
    "DX CINNAMON DANISH": [
        "gallon - $105.00 (USD)",
        "case (4) 2week lead time - $380.00 (USD)",
    ],
    "DX COCONUT CANDY FLAVOR": [
        "gallon - $110.00 (USD)",
        "case (4) 2week lead time - $400.00 (USD)",
        "double case (8) 2 week lead time - $737.20 (USD)",
    ],
    "DX COCONUT FLAVOR": [
        "gallon - $110.00 (USD)",
        "case (4) 2week lead time - $420.00 (USD)",
        "double case (8) 2 week lead time - $800.00 (USD)",
    ],
    "DX FROSTED DONUT FLAVOR": [
        "gallon - $100.00 (USD)",
        "case (4) 2week lead time - $375.00 (USD)",
        "double case (8) 2 week lead time - $742.00 (USD)",
    ],
    "DX GRAHAM CRACKER FLAVOR": [
        "gallon - $119.70 (USD)",
        "case (4) 2week lead time - $454.80 (USD)",
    ],
    "DX HAZELNUT FLAVOR": [
        "gallon - $96.90 (USD)",
        "case (4 gallons) - $376.00 (USD)",
        "double case (8) 2 week lead time - $736.00 (USD)",
    ],
    "DX JAMAICAN RUM FLAVOR": [
        "gallon - $129.00 (USD)",
        "case (4) 2week lead time - $480.00 (USD)",
    ],
    "DX MARSHMALLOW FLAVOR": [
        "gallon - $110.00 (USD)",
        "case (4) 2week lead time - $400.00 (USD)",
    ],
    "DX MILK CHOCOLATE FLAVOR": [
        "gallon - $126.50 (USD)",
        "case (4) 2week lead time - $492.00 (USD)",
    ],
    "DX MILK FLAVOR": [
        "gallon - $102.60 (USD)",
        "case (4) 2week lead time - $396.00 (USD)",
        "double case (8) 2 week lead time - $776.00 (USD)",
    ],
    "DX PEACH (JUICY) FLAVOR": [
        "gallon - $84.00 (USD)",
        "case (4 gallons) - $364.00 (USD)",
        "double case (8) 2 week lead time - $712.00 (USD)",
    ],
    "DX PEANUT BUTTER FLAVOR": [
        "gallon - $102.60 (USD)",
        "case (4 gallons) - $400.00 (USD)",
        "double case (8) 2 week lead time - $784.00 (USD)",
    ],
    "DX SWEET CREAM FLAVOR": [
        "gallon - $102.60 (USD)",
        "case (4) 2week lead time - $400.00 (USD)",
        "double case (8) 2 week lead time - $784.00 (USD)",
    ],
    "DX VANILLA CUPCAKE": [
        "gallon - $105.00 (USD)",
        "case (4 gallons) - $380.00 (USD)",
        "double case (8) 2 week lead time - $712.00 (USD)",
    ],
    "EARL GREY TEA FLAVOR **": [
        "gallon - $148.20 (USD)",
        "case (4) 2week lead time - $572.80 (USD)",
    ],
    "EARL GREY TEA II FLAVOR": [
        "gallon - $148.20 (USD)",
        "case (4) 2week lead time - $572.80 (USD)",
    ],
    "EGG NOG FLAVOR": ["gallon - $114.00 (USD)"],
    "ELDERBERRY FLAVOR": [
        "gallon - $96.90 (USD)",
        "case (4) 2week lead time - $372.00 (USD)",
    ],
    "ENERGY DRINK FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4 gallons) - $332.00 (USD)",
        "double case (8) 2 week lead time - $640.00 (USD)",
    ],
    "ENGLISH TOFFEE FLAVOR": [
        "gallon - $114.00 (USD)",
        "case (4) 2week lead time - $452.00 (USD)",
        "double case (8) 2 week lead time - $896.00 (USD)",
    ],
    "ESPRESSO FLAVOR": [
        "gallon - $96.90 (USD)",
        "case (4) 2week lead time - $376.00 (USD)",
    ],
    "FRENCH VANILLA CREME": [
        "gallon - $114.00 (USD)",
        "case (4 gallons) - $420.00 (USD)",
        "double case (8) 2 week lead time - $800.00 (USD)",
    ],
    "FRENCH VANILLA DELUXE FLAVOR": [
        "gallon - $114.00 (USD)",
        "case (4) 2week lead time - $444.00 (USD)",
        "double case (8) 2 week lead time - $872.00 (USD)",
    ],
    "FRENCH VANILLA FLAVOR": [
        "gallon - $96.90 (USD)",
        "case (4 gallons) - $376.00 (USD)",
        "double case (8) 2 week lead time - $736.00 (USD)",
    ],
    "FRENCH VANILLA II FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $300.00 (USD)",
        "double case (8) 2 week lead time - $560.00 (USD)",
    ],
    "FRESH MINT FLAVOR CC": ["gallon - $120.00 (USD)"],
    "FROSTED DONUT FLAVOR": [
        "gallon - $105.00 (USD)",
        "case (4 gallons) - $380.00 (USD)",
        "double case (8) 2 week lead time - $720.00 (USD)",
        "petuk 66",
    ],
    "FRUIT CIRCLES FLAVOR": [
        "gallon - $114.00 (USD)",
        "case (4 gallons) - $448.00 (USD)",
        "double case (8) 2 week lead time - $880.00 (USD)",
    ],
    "FRUIT CIRCLES WITH MILK FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $300.00 (USD)",
        "double case (8) 2 week lead time - $584.00 (USD)",
    ],
    "FRUIT SMOOTHIE FLAVOR**": [
        "gallon - $102.60 (USD)",
        "case (4 gallons) - $360.00 (USD)",
        "double case (8) 2 week lead time - $719.78 (USD)",
    ],
    "FRUITY STICK GUM FLAVOR": [
        "gallon - $105.50 (USD)",
        "case (4) 2week lead time - $412.00 (USD)",
        "double case (8) 2 week lead time - $808.00 (USD)",
    ],
    "GINGER ALE FLAVOR (NF)": [
        "gallon - $129.00 (USD)",
        "case (4) 2week lead time - $390.00 (USD)",
    ],
    "GINGER ALE FLAVOR **": ["gallon - $129.00 (USD)"],
    "GINGERBREAD COOKIE": [
        "gallon - $185.00 (USD)",
        "case (4) 2week lead time - $592.00 (USD)",
    ],
    "GINGERBREAD EXTRA GINGER FLAVOR": [
        "gallon - $124.00 (USD)",
        "case (4) 2week lead time - $484.00 (USD)",
        "double case (8) 2 week lead time - $944.00 (USD)",
    ],
    "GRAHAM CRACKER CLEAR": [
        "gallon - $107.90 (USD)",
        "case (4 gallons) - $424.00 (USD)",
        "double case (8) 2 week lead time - $836.00 (USD)",
    ],
    "GRAHAM CRACKER FLAVOR": [
        "gallon - $119.70 (USD)",
        "case (4) 2week lead time - $454.80 (USD)",
        "double case (8) 2 week lead time - $894.00 (USD)",
    ],
    "GRAPE CANDY FLAVOR**": [
        "gallon - $92.00 (USD)",
        "case (4 gallons) - $356.00 (USD)",
        "double case (8) 2 week lead time - $696.00 (USD)",
    ],
    "CONCORD GRAPE JUICE FLAVOR **": [
        "gallon - $119.70 (USD)",
        "case (4) 2week lead time - $468.00 (USD)",
        "double case (8) 2 week lead time - $920.00 (USD)",
    ],
    "GRAPE JUICE FLAVOR**": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $336.00 (USD)",
        "double case (8) 2 week lead time - $652.00 (USD)",
    ],
    "GRAPE SODA FLAVOR": [
        "gallon - $130.00 (USD)",
        "case (4 gallons) - $475.00 (USD)",
        "double case (8) 2 week lead time - $896.00 (USD)",
    ],
    "GREEK YOGURT FLAVOR": [
        "gallon - $132.00 (USD)",
        "case (4 gallons) - $524.00 (USD)",
        "double case (8) 2 week lead time - $1,040.00 (USD)",
    ],
    "GREEN APPLE FLAVOR": [
        "gallon - $96.90 (USD)",
        "case (4 gallons) - $376.00 (USD)",
        "double case (8) 2 week lead time - $736.00 (USD)",
    ],
    "GREEN TEA FLAVOR": [
        "gallon - $202.50 (USD)",
        "case (4) 2week lead time - $760.00 (USD)",
        "double case (8) 2 week lead time - $1,480.00 (USD)",
    ],
    "GUAVA FLAVOR": [
        "gallon - $129.00 (USD)",
        "case (4) 2week lead time - $496.00 (USD)",
    ],
    "GUMMY CANDY (PG) FLAVOR": [
        "gallon - $96.30 (USD)",
        "case (4 gallons) - $345.20 (USD)",
        "double case (8) 2 week lead time - $650.40 (USD)",
    ],
    "GUMMY CANDY FLAVOR": [
        "gallon - $96.90 (USD)",
        "case (4) 2week lead time - $347.60 (USD)",
    ],
    "HAWAIIAN DRINK FLAVOR**": [
        "gallon - $162.00 (USD)",
        "case (4) 2week lead time - $640.00 (USD)",
        "double case (8) 2 week lead time - $1,264.00 (USD)",
    ],
    "HAZELNUT FLAVOR": [
        "gallon - $96.90 (USD)",
        "case (4 gallons) - $347.60 (USD)",
        "double case (8) 2 week lead time - $672.00 (USD)",
    ],
    "HAZELNUT PRALINE FLAVOR": [
        "gallon - $134.60 (USD)",
        "case (4) 2week lead time - $532.00 (USD)",
    ],
    "HIBISCUS FLAVOR": [
        "gallon - $105.00 (USD)",
        "case (4) 2week lead time - $380.00 (USD)",
        "double case (8) 2 week lead time - $744.00 (USD)",
    ],
    "HICKORY SMOKE FLAVOR": ["gallon - $97.10 (USD)"],
    "HONEY CIRCLES CEREAL FLAVOR": [
        "gallon - $129.00 (USD)",
        "case (4) 2week lead time - $480.00 (USD)",
        "double case (8) 2 week lead time - $945.00 (USD)",
    ],
    "HONEY FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $302.00 (USD)",
    ],
    "HONEY ORANGE TOBACCO TYPE FLAVOR CC": ["gallon - $280.00 (USD)"],
    "HONEY TOBACCO TYPE FLAVOR CC": [
        "gallon - $210.00 (USD)",
        "case (4) 2week lead time - $828.00 (USD)",
    ],
    "HONEYDEW FLAVOR **": [
        "gallon - $290.00 (USD)",
        "case (4) 2week lead time - $1,120.00 (USD)",
        "double case (8) 2 week lead time - $2,160.00 (USD)",
    ],
    "HONEYDEW II FLAVOR": [
        "gallon - $195.80 (USD)",
        "case (4 gallons) - $776.00 (USD)",
        "double case (8) 2 week lead time - $1,544.00 (USD)",
    ],
    "HONEYSUCKLE FLAVOR (PG)": [
        "gallon - $129.00 (USD)",
        "case (4) 2week lead time - $476.00 (USD)",
        "double case (8) 2 week lead time - $912.00 (USD)",
    ],
    "HORCHATA SMOOTH FLAVOR": [
        "gallon - $139.30 (USD)",
        "case (4) 2week lead time - $552.00 (USD)",
    ],
    "HOREHOUND FLAVOR **": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $320.00 (USD)",
    ],
    "HPNO II FLAVOR": [
        "gallon - $103.20 (USD)",
        "case (4) 2week lead time - $400.00 (USD)",
        "double case (8) 2 week lead time - $784.00 (USD)",
    ],
    "HPNO TYPE FLAVOR **": [
        "gallon - $91.20 (USD)",
        "case (4) 2week lead time - $324.80 (USD)",
    ],
    "HUCKLEBERRY FLAVOR**": [
        "gallon - $96.90 (USD)",
        "case (4) 2week lead time - $360.00 (USD)",
    ],
    "IRISH CREAM FLAVOR **": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $302.00 (USD)",
        "double case (8) 2 week lead time - $547.08 (USD)",
    ],
    "IRISH CREAM II FLAVOR": [
        "gallon - $107.75 (USD)",
        "case (4) 2week lead time - $416.00 (USD)",
    ],
    "JACKFRUIT FLAVOR": [
        "gallon - $120.00 (USD)",
        "case (4) 2week lead time - $474.00 (USD)",
        "double case (8) 2 week lead time - $936.00 (USD)",
    ],
    "JAMAICAN RUM FLAVOR **": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $316.50 (USD)",
    ],
    "KALUA AND CREAM FLAVOR": [
        "gallon - $185.00 (USD)",
        "case (4) 2week lead time - $592.00 (USD)",
    ],
    "KENTUCKY BOURBON FLAVOR **": [
        "gallon - $102.60 (USD)",
        "case (4) 2week lead time - $370.40 (USD)",
    ],
    "KETTLE CORN FLAVOR": [
        "gallon - $91.00 (USD)",
        "case (4) 2week lead time - $324.00 (USD)",
        "double case (8) 2 week lead time - $632.00 (USD)",
    ],
    "KEY LIME FLAVOR **": [
        "gallon - $85.50 (USD)",
        "case (4 gallons) - $332.00 (USD)",
        "double case (8) 2 week lead time - $648.00 (USD)",
    ],
    "KEY LIME PIE FLAVOR": [
        "gallon - $133.10 (USD)",
        "case (4) 2week lead time - $528.00 (USD)",
        "double case (8) 2 week lead time - $1,040.00 (USD)",
    ],
    "KIWI (DOUBLE) FLAVOR": [
        "gallon - $98.00 (USD)",
        "case (4 gallons) - $384.00 (USD)",
        "double case (8) 2 week lead time - $752.00 (USD)",
    ],
    "KOOLADA 10 PG": [
        "gallon - $145.00 (USD)",
        "case (4 gallons) - $570.00 (USD)",
        "double case (8) 2 week lead time - $1,120.00 (USD)",
    ],
    "LAVENDER FLAVOR": [
        "gallon - $105.00 (USD)",
        "case (4) 2week lead time - $380.00 (USD)",
    ],
    "LEMON (WATER SOLUBLE) FLAVOR **": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $336.00 (USD)",
        "double case (8) 2 week lead time - $656.00 (USD)",
    ],
    "LEMON II FLAVOR": [
        "gallon - $115.70 (USD)",
        "case (4) 2week lead time - $456.00 (USD)",
        "double case (8) 2 week lead time - $904.00 (USD)",
    ],
    "LEMON LIME FLAVOR**": [
        "gallon - $96.90 (USD)",
        "case (4) 2week lead time - $347.60 (USD)",
        "double case (8) 2 week lead time - $687.20 (USD)",
    ],
    "LEMON LIME II FLAVOR": [
        "gallon - $116.60 (USD)",
        "case (4) 2week lead time - $460.00 (USD)",
        "double case (8) 2 week lead time - $912.00 (USD)",
    ],
    "LEMONADE COOKIE FLAVOR": [
        "gallon - $129.00 (USD)",
        "case (4) 2week lead time - $476.00 (USD)",
        "double case (8) 2 week lead time - $936.00 (USD)",
    ],
    "LICORICE TOBACCO FLAVOR CC": ["gallon - $119.70 (USD)"],
    "LUCKY LEPRECHAUN CEREAL FLAVOR": [
        "gallon - $95.00 (USD)",
        "case (4 gallons) - $340.00 (USD)",
        "double case (8) 2 week lead time - $656.00 (USD)",
    ],
    "LYCHEE FLAVOR": [
        "gallon - $96.00 (USD)",
        "case (4) 2week lead time - $372.00 (USD)",
    ],
    "MALTED MILK (CONC) FLAVOR": [
        "gallon - $102.00 (USD)",
        "case (4 gallons) - $380.00 (USD)",
        "double case (8) 2 week lead time - $720.00 (USD)",
    ],
    "MANGO FLAVOR": [
        "gallon - $95.00 (USD)",
        "case (4 gallons) - $368.00 (USD)",
        "double case (8) 2 week lead time - $712.00 (USD)",
    ],
    "MAPLE DELUXE FLAVOR": [
        "gallon - $125.90 (USD)",
        "case (4) 2week lead time - $500.00 (USD)",
        "double case (8) 2 week lead time - $984.00 (USD)",
    ],
    "MAPLE FLAVOR**": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $302.00 (USD)",
    ],
    "MAPLE SYRUP FLAVOR": [
        "gallon - $91.20 (USD)",
        "case (4) 2week lead time - $324.80 (USD)",
        "double case (8) 2 week lead time - $600.00 (USD)",
    ],
    "MARASCHINO CHERRY (PG)": [
        "gallon - $96.90 (USD)",
        "case (4) 2week lead time - $347.60 (USD)",
    ],
    "MARSHMALLOW FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4 gallons) - $336.00 (USD)",
        "double case (8) 2 week lead time - $656.00 (USD)",
    ],
    "MARY JANE FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $302.00 (USD)",
        "double case (8) 2 week lead time - $584.00 (USD)",
    ],
    "MENTHOL LIQUID (PG)": [
        "gallon - $290.00 (USD)",
        "case (4 gallons) - $1,144.00 (USD)",
        "double case (8) 2 week lead time - $2,256.00 (USD)",
    ],
    "MERINGUE FLAVOR": [
        "gallon - $123.00 (USD)",
        "case (4 gallons) - $488.00 (USD)",
        "double case (8) 2 week lead time - $968.00 (USD)",
    ],
    "MEXICAN COFFEE FLAVOR": ["gallon - $105.00 (USD)"],
    "MIDWEST TOBACCO TYPE FLAVOR CC": ["gallon - $240.00 (USD)"],
    "MILK CHOCOLATE FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4 gallons) - $332.00 (USD)",
        "double case (8) 2 week lead time - $648.00 (USD)",
    ],
    "MINT CANDY FLAVOR": [
        "gallon - $120.00 (USD)",
        "case (4) 2week lead time - $440.00 (USD)",
        "double case (8) 2 week lead time - $800.00 (USD)",
    ],
    "MINT FLAVOR CC": ["gallon - $99.75 (USD)"],
    "MOCHA FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $328.00 (USD)",
    ],
    "MOJITO FLAVOR **": [
        "gallon - $129.00 (USD)",
        "case (4 gallons) - $460.00 (USD)",
        "double case (8) 2 week lead time - $896.00 (USD)",
    ],
    "MOJITO HAVANA FLAVOR": [
        "gallon - $143.80 (USD)",
        "case (4) 2week lead time - $568.00 (USD)",
        "double case (8) 2 week lead time - $1,128.00 (USD)",
    ],
    "MOLASSES FLAVOR": [
        "gallon - $86.00 (USD)",
        "case (4) 2week lead time - $304.00 (USD)",
    ],
    "MUSK CANDY FLAVOR": ["gallon - $120.00 (USD)"],
    "NECTARINE FLAVOR": [
        "gallon - $119.70 (USD)",
        "case (4 gallons) - $438.80 (USD)",
        "double case (8) 2 week lead time - $837.60 (USD)",
    ],
    "OATMEAL COOKIE FLAVOR": [
        "gallon - $120.00 (USD)",
        "case (4) 2week lead time - $475.00 (USD)",
        "double case (8) 2 week lead time - $904.00 (USD)",
    ],
    "BLOOD ORANGE FLAVOR": [
        "gallon - $110.00 (USD)",
        "case (4 gallons) - $400.00 (USD)",
    ],
    "DX PISTACHIO FLAVOR": ["case (4) 2week lead time - $387.60 (USD)"],
    "ORANGE CREAM BAR FLAVOR": [
        "gallon - $110.00 (USD)",
        "case (4) 2week lead time - $428.00 (USD)",
        "double case (8) 2 week lead time - $840.00 (USD)",
    ],
    "ORANGE CREAM FLAVOR **": [
        "gallon - $85.50 (USD)",
        "case (4 gallons) - $300.00 (USD)",
        "double case (8) 2 week lead time - $587.08 (USD)",
    ],
    "ORANGE MANDARIN FLAVOR": [
        "gallon - $110.00 (USD)",
        "case (4 gallons) - $400.00 (USD)",
        "double case (8) 2 week lead time - $776.00 (USD)",
    ],
    "ORGANIC COMPLIANT STRAWBERRY FLAVOR **": [
        "gallon - $162.90 (USD)",
        "case (4) 2week lead time - $640.00 (USD)",
    ],
    "PANCAKE FLAVOR": [
        "gallon - $130.00 (USD)",
        "case (4) 2week lead time - $500.00 (USD)",
    ],
    "PAPAYA FLAVOR": [
        "gallon - $97.00 (USD)",
        "case (4 gallons) - $380.00 (USD)",
        "double case (8) 2 week lead time - $744.00 (USD)",
    ],
    "PAPAYA II FLAVOR": ["gallon - $97.00 (USD)", "case (4 gallons) - $348.00 (USD)"],
    "PASSION FRUIT FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $328.00 (USD)",
    ],
    "PASSION ORANGE GUAVA FLAVOR": [
        "gallon - $119.00 (USD)",
        "case (4 gallons) - $464.00 (USD)",
        "double case (8) 2 week lead time - $912.00 (USD)",
    ],
    "PEACH (JUICY) FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $332.00 (USD)",
        "double case (8) 2 week lead time - $648.00 (USD)",
    ],
    "PEACH FLAVOR": [
        "gallon - $88.00 (USD)",
        "case (4 gallons) - $344.00 (USD)",
        "double case (8) 2 week lead time - $672.00 (USD)",
    ],
    "PEACH YOGURT FLAVOR": [
        "gallon - $119.00 (USD)",
        "case (4 gallons) - $464.00 (USD)",
        "double case (8) 2 week lead time - $912.00 (USD)",
    ],
    "PEANUT BUTTER FLAVOR": [
        "gallon - $102.60 (USD)",
        "case (4 gallons) - $400.00 (USD)",
        "double case (8) 2 week lead time - $784.00 (USD)",
    ],
    "PEAR CANDY FLAVOR": [
        "gallon - $96.90 (USD)",
        "case (4) 2week lead time - $368.00 (USD)",
        "double case (8) 2 week lead time - $720.00 (USD)",
    ],
    "PEAR FLAVOR": [
        "gallon - $160.00 (USD)",
        "case (4 gallons) - $628.00 (USD)",
        "double case (8) - $1,240.00 (USD)",
    ],
    "PECAN FLAVOR": [
        "gallon - $125.00 (USD)",
        "case (4) 2week lead time - $400.00 (USD)",
    ],
    "PEPPERMINT FLAVOR **": [
        "gallon - $125.40 (USD)",
        "case (4 gallons) - $481.60 (USD)",
        "double case (8) 2 week lead time - $936.00 (USD)",
    ],
    "PEPPERMINT II FLAVOR": [
        "gallon - $135.00 (USD)",
        "case (4) 2week lead time - $520.00 (USD)",
        "double case (8) 2 week lead time - $1,000.00 (USD)",
    ],
    "PHILIPPINE MANGO FLAVOR": [
        "gallon - $90.00 (USD)",
        "case (4) 2week lead time - $340.00 (USD)",
        "double case (8) 2 week lead time - $656.00 (USD)",
    ],
    "PIE CRUST FLAVOR": [
        "gallon - $119.70 (USD)",
        "case (4 gallons) - $438.80 (USD)",
        "double case (8) 2 week lead time - $835.00 (USD)",
    ],
    "PINA COLADA FLAVOR": [
        "gallon - $119.70 (USD)",
        "case (4 gallons) - $436.00 (USD)",
        "double case (8) 2 week lead time - $840.00 (USD)",
    ],
    "PINEAPPLE FLAVOR **": [
        "gallon - $102.60 (USD)",
        "case (4 gallons) - $400.00 (USD)",
        "double case (8) 2 week lead time - $776.00 (USD)",
    ],
    "PINEAPPLE JUICY FLAVOR": [
        "gallon - $135.00 (USD)",
        "case (4 gallons) - $532.00 (USD)",
        "double case (8) 2 week lead time - $1,056.00 (USD)",
    ],
    "PISTACHIO FLAVOR": [
        "gallon - $96.90 (USD)",
        "case (4 gallons) - $347.60 (USD)",
        "double case (8) 2 week lead time - $656.00 (USD)",
    ],
    "PLUM FLAVOR (PG)": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $302.00 (USD)",
    ],
    "POMEGRANATE DELUXE": [
        "gallon - $119.70 (USD)",
        "case (4 gallons) - $438.80 (USD)",
        "double case (8) 2 week lead time - $837.60 (USD)",
    ],
    "POMEGRANATE FLAVOR": [
        "gallon - $119.70 (USD)",
        "case (4 gallons) - $440.00 (USD)",
        "double case (8) 2 week lead time - $852.47 (USD)",
    ],
    "POPCORN AIR POPPED FLAVOR": [
        "gallon - $179.45 (USD)",
        "case (4) 2week lead time - $696.00 (USD)",
    ],
    "POPCORN FLAVOR": [
        "gallon - $125.40 (USD)",
        "case (4) 2week lead time - $481.60 (USD)",
        "double case (8) 2 week lead time - $918.78 (USD)",
    ],
    "POPCORN MOVIE THEATER FLAVOR": [
        "gallon - $114.00 (USD)",
        "case (4) 2week lead time - $416.00 (USD)",
    ],
    "PUMPKIN FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $302.00 (USD)",
    ],
    "PUMPKIN SPICE FLAVOR **": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $302.00 (USD)",
    ],
    "QUINCE FLAVOR **": [
        "gallon - $105.00 (USD)",
        "case (4) 2week lead time - $380.00 (USD)",
    ],
    "RAINBOW DROPS FLAVOR (NF)": [
        "gallon - $135.00 (USD)",
        "case (4) 2week lead time - $528.00 (USD)",
    ],
    "RAINBOW DROPS FLAVOR **": [
        "gallon - $129.00 (USD)",
        "case (4 gallons) - $512.00 (USD)",
        "double case (8) 2 week lead time - $1,016.00 (USD)",
    ],
    "RAINBOW SHERBET FLAVOR": [
        "gallon - $114.00 (USD)",
        "case (4 gallons) - $440.00 (USD)",
        "double case (8) 2 week lead time - $856.00 (USD)",
    ],
    "RAISIN FLAVOR": [
        "gallon - $119.70 (USD)",
        "case (4) 2week lead time - $460.00 (USD)",
    ],
    "RASPBERRY (SWEET) FLAVOR": [
        "gallon - $97.00 (USD)",
        "case (4 gallons) - $348.00 (USD)",
        "double case (8) 2 week lead time - $636.32 (USD)",
    ],
    "RASPBERRY FLAVOR**": [
        "gallon - $129.00 (USD)",
        "case (4) 2week lead time - $500.00 (USD)",
        "double case (8) 2 week lead time - $960.00 (USD)",
        "piiiituk 66",
    ],
    "RED LICORICE FLAVOR": [
        "gallon - $102.60 (USD)",
        "case (4) 2week lead time - $360.00 (USD)",
        "double case (8) 2 week lead time - $656.00 (USD)",
    ],
    "RED OAK FLAVOR": [
        "gallon - $119.70 (USD)",
        "case (4) 2week lead time - $438.80 (USD)",
        "double case (8) 2 week lead time - $840.00 (USD)",
    ],
    "RED TYPE BLEND": [
        "gallon - $185.00 (USD)",
        "case (4) 2week lead time - $720.00 (USD)",
    ],
    "RICE CRUNCHIES FLAVOR": [
        "gallon - $138.00 (USD)",
        "case (4 gallons) - $544.00 (USD)",
        "double case (8) 2 week lead time - $1,080.00 (USD)",
    ],
    "RIPE BANANA FLAVOR **": [
        "gallon - $99.75 (USD)",
        "case (4) 2week lead time - $359.00 (USD)",
        "double case (8) 2 week lead time - $670.00 (USD)",
    ],
    "ROOT BEER FLAVOR (NF)": [
        "gallon - $135.00 (USD)",
        "case (4) 2week lead time - $528.00 (USD)",
        "double case (8) 2 week lead time - $1,040.00 (USD)",
    ],
    "ROOT BEER FLAVOR (PG) **": [
        "gallon - $125.00 (USD)",
        "case (4) 2week lead time - $488.00 (USD)",
        "double case (8) 2 week lead time - $952.00 (USD)",
    ],
    "ROOT BEER FLAVOR (TRI)": ["gallon - $125.00 (USD)"],
    "ROOT BEER FLOAT FLAVOR": [
        "gallon - $129.00 (USD)",
        "case (4) 2week lead time - $450.00 (USD)",
    ],
    "ROSE CANDY FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $302.00 (USD)",
    ],
    "RUBY CHOCOLATE FLAVOR": ["gallon - $114.00 (USD)"],
    "RY4 ASIAN FLAVOR": [
        "gallon - $132.00 (USD)",
        "case (4) 2week lead time - $488.00 (USD)",
        "double case (8) 2 week lead time - $944.00 (USD)",
    ],
    "RY4 DOUBLE FLAVOR": [
        "gallon - $119.00 (USD)",
        "case (4) 2week lead time - $464.00 (USD)",
        "double case (8) 2 week lead time - $904.00 (USD)",
    ],
    "RY4 TYPE FLAVOR**": [
        "gallon - $135.00 (USD)",
        "case (4) 2week lead time - $528.00 (USD)",
        "double case (8) 2 week lead time - $1,040.00 (USD)",
    ],
    "SAFFRON FLAVOR": ["gallon - $148.00 (USD)"],
    "SEA BUCKTHORN FLAVOR": ["gallon - $105.00 (USD)"],
    "SILLY RABBIT CEREAL FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $320.00 (USD)",
    ],
    "SLIM MINT COOKIE FLAVOR": ["gallon - $314.05 (USD)"],
    "SMOOTH FLAVOR": [
        "gallon - $105.00 (USD)",
        "case (4) 2week lead time - $380.00 (USD)",
        "double case (8) 2 week lead time - $738.40 (USD)",
    ],
    "SOUR FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4 gallons) - $332.00 (USD)",
        "double case (8) 2 week lead time - $648.00 (USD)",
    ],
    "SPEARMINT DELUXE FLAVOR CC": ["gallon - $119.70 (USD)"],
    "SPEARMINT FLAVOR": [
        "gallon - $130.00 (USD)",
        "case (4) 2week lead time - $500.00 (USD)",
        "double case (8) 2 week lead time - $976.00 (USD)",
    ],
    "SPEARMINT MENTHOL FLAVOR CC": ["gallon - $119.70 (USD)"],
    "SPURBERRY FLAVOR**": [
        "gallon - $145.70 (USD)",
        "case (4 gallons) - $576.00 (USD)",
        "double case (8) 2 week lead time - $1,144.00 (USD)",
    ],
    "STRAWBERRIES AND CREAM FLAVOR": [
        "gallon - $96.90 (USD)",
        "case (4 gallons) - $376.00 (USD)",
        "double case (8) 2 week lead time - $736.00 (USD)",
    ],
    "STRAWBERRY (RIPE) FLAVOR": [
        "gallon - $119.70 (USD)",
        "case (4 gallons) - $468.00 (USD)",
        "double case (8) 2 week lead time - $920.00 (USD)",
    ],
    "STRAWBERRY FLAVOR": [
        "gallon - $105.00 (USD)",
        "case (4) - $408.00 (USD)",
        "double case (8) 2 week lead time - $800.00 (USD)",
    ],
    "STRAWBERRY LEMONADE FLAVOR": [
        "gallon - $119.00 (USD)",
        "case (4 gallons) - $464.00 (USD)",
        "double case (8) 2 week lead time - $904.00 (USD)",
    ],
    "STRAWBERRY YOGURT FLAVOR": [
        "gallon - $140.90 (USD)",
        "case (4 gallons) - $556.00 (USD)",
        "double case (8) 2 week lead time - $1,104.00 (USD)",
    ],
    "SUPER SWEETENER": [
        "gallon - $115.00 (USD)",
        "case (4 gallons) - $440.00 (USD)",
        "double case (8) 2 week lead time - $840.00 (USD)",
    ],
    "SWEDISH GUMMY FLAVOR": [
        "gallon - $120.00 (USD)",
        "case (4 gallons) - $472.00 (USD)",
        "double case (8) 2 week lead time - $936.00 (USD)",
    ],
    "SWEET AND TART FLAVOR": [
        "gallon - $105.00 (USD)",
        "case (4 gallons) - $380.00 (USD)",
        "double case (8) 2 week lead time - $698.40 (USD)",
    ],
    "SWEET CEREAL FLAKES FLAVOR": [
        "gallon - $120.00 (USD)",
        "case (4 gallons) - $435.00 (USD)",
        "double case (8) 2 week lead time - $814.80 (USD)",
    ],
    "SWEET CREAM FLAVOR": [
        "gallon - $102.60 (USD)",
        "case (4 gallons) - $400.00 (USD)",
        "double case (8) 2 week lead time - $784.00 (USD)",
    ],
    "SWEET STRAWBERRY FLAVOR**": [
        "gallon - $114.00 (USD)",
        "case (4) 2week lead time - $416.00 (USD)",
        "double case (8) 2 week lead time - $784.00 (USD)",
    ],
    "SWEET TEA FLAVOR": [
        "gallon - $143.10 (USD)",
        "case (4) 2week lead time - $568.00 (USD)",
        "double case (8) 2 week lead time - $1,120.00 (USD)",
    ],
    "SWEET TOBACCO TYPE FLAVOR CC": ["gallon - $240.00 (USD)"],
    "SWEETENER": [
        "gallon - $85.50 (USD)",
        "case (4 gallons) - $336.00 (USD)",
        "double case (8) 2 week lead time - $656.00 (USD)",
    ],
    "TARO FLAVOR": [
        "gallon - $100.00 (USD)",
        "case (4) 2week lead time - $360.00 (USD)",
        "double case (8) 2 week lead time - $680.00 (USD)",
    ],
    "TART AND SOUR FLAVOR": [
        "gallon - $122.00 (USD)",
        "case (4 gallons) - $484.00 (USD)",
        "double case (8) 2 week lead time - $960.00 (USD)",
    ],
    "TIRAMISU FLAVOR": ["gallon - $180.00 (USD)"],
    "TOASTED ALMOND FLAVOR": [
        "gallon - $132.00 (USD)",
        "case (4 gallons) - $514.00 (USD)",
        "double case (8) 2 week lead time - $960.00 (USD)",
    ],
    "TOASTED MARSHMALLOW FLAVOR": [
        "gallon - $129.00 (USD)",
        "case (4 gallons) - $508.00 (USD)",
        "double case (8) 2 week lead time - $986.00 (USD)",
    ],
    "TOBACCO FLAVOR": [
        "gallon - $102.60 (USD)",
        "case (4) 2week lead time - $370.40 (USD)",
        "double case (8) 2 week lead time - $719.78 (USD)",
    ],
    "TOBACCO TYPE FLAVOR CC": ["gallon - $148.00 (USD)"],
    "TURKISH FLAVOR": [
        "gallon - $129.00 (USD)",
        "case (4) 2week lead time - $500.00 (USD)",
        "double case (8) 2 week lead time - $920.00 (USD)",
    ],
    "TUTTI FRUTTI DELUXE FLAVOR": [
        "gallon - $114.00 (USD)",
        "case (4) 2week lead time - $450.00 (USD)",
        "double case (8) 2 week lead time - $880.00 (USD)",
    ],
    "TUTTI-FRUTTI FLAVOR **": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $302.00 (USD)",
        "double case (8) 2 week lead time - $584.00 (USD)",
    ],
    "MADAGASCAR BOURBON VANILLA FLAVOR": [
        "gallon - $242.85 (USD)",
        "case (4) 2week lead time - $952.00 (USD)",
    ],
    "VANILLA BEAN GELATO FLAVOR": [
        "gallon - $168.00 (USD)",
        "case (4 gallons) - $664.00 (USD)",
        "double case (8) 2 week lead time - $1,312.00 (USD)",
    ],
    "VANILLA BEAN ICE CREAM FLAVOR": [
        "gallon - $125.40 (USD)",
        "case (4 gallons) - $461.60 (USD)",
        "double case (8) 2 week lead time - $864.00 (USD)",
    ],
    "VANILLA CUPCAKE": [
        "gallon - $102.00 (USD)",
        "case (4) 2week lead time - $380.00 (USD)",
        "double case (8) 2 week lead time - $675.12 (USD)",
    ],
    "VANILLA CUSTARD FLAVOR": [
        "gallon - $130.00 (USD)",
        "case (4) 2week lead time - $504.00 (USD)",
        "double case (8) 2 week lead time - $984.00 (USD)",
    ],
    "VANILLA CUSTARD II FLAVOR": [
        "gallon - $142.50 (USD)",
        "case (4) 2week lead time - $554.00 (USD)",
    ],
    "VANILLA SWIRL FLAVOR": [
        "gallon - $120.00 (USD)",
        "case (4 gallons) - $440.00 (USD)",
        "double case (8) 2 week lead time - $820.00 (USD)",
    ],
    "VANILLIN 10 (PG)": [
        "gallon - $84.00 (USD)",
        "case (4 gallons) - $328.00 (USD)",
        "double case (8) 2 week lead time - $640.00 (USD)",
    ],
    "WAFFLE (BELGIAN) FLAVOR": [
        "gallon - $129.00 (USD)",
        "case (4) 2week lead time - $476.00 (USD)",
        "double case (8) 2 week lead time - $920.00 (USD)",
    ],
    "WAFFLE FLAVOR **": [
        "gallon - $91.20 (USD)",
        "case (4) 2week lead time - $356.00 (USD)",
    ],
    "WATERMELON (VG) FLAVOR": [
        "gallon - 2 week lead time - $85.50 (USD)",
        "case (4) 2week lead time - $302.00 (USD)",
    ],
    "WATERMELON CANDY FLAVOR": [
        "gallon - $120.00 (USD)",
        "case (4 gallons) - $440.00 (USD)",
        "double case (8) 2 week lead time - $807.04 (USD)",
    ],
    "WATERMELON FLAVOR": [
        "gallon - $142.50 (USD)",
        "case (4 gallons) - $556.00 (USD)",
        "double case (8) 2 week lead time - $1,096.00 (USD)",
    ],
    "WESTERN FLAVOR": [
        "gallon - $148.20 (USD)",
        "case (4) 2week lead time - $520.00 (USD)",
        "double case (8) 2 week lead time - $931.20 (USD)",
    ],
    "WESTERN FLAVOR CC": ["gallon - $148.20 (USD)"],
    "WESTERN II FLAVOR": [
        "gallon - $148.20 (USD)",
        "case (4) 2week lead time - $520.00 (USD)",
        "double case (8) 2 week lead time - $931.20 (USD)",
    ],
    "WHIPPED CREAM FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $316.50 (USD)",
        "double case (8) 2 week lead time - $547.08 (USD)",
    ],
    "WHITE CHOCOLATE FLAVOR": [
        "gallon - $85.50 (USD)",
        "case (4) 2week lead time - $300.00 (USD)",
        "double case (8) 2 week lead time - $524.00 (USD)",
    ],
    "WINTERGREEN DELUXE FLAVOR CC": ["gallon - $125.00 (USD)"],
    "WINTERGREEN FLAVOR": [
        "gallon - $875.50 (USD)",
        "case (4) 2week lead time - $300.00 (USD)",
        "piiituuuuhhhh 887"
    ],
    "WS-23 30%": [
        "gallon - $240.00 (USD)",
        "case (4) 2week lead time - $928.00 (USD)",
        "double case (8) 2 week lead time - $1,848.00 (USD)",
    ],
    "YAM FLAVOR": [
        "gallon - $102.00 (USD)",
        "case (4) 2week lead time - $375.00 (USD)",
        "double case (8) 2 week lead time - $720.00 (USD)",
    ],
    "ZESTY TOBACCO TYPE FLAVOR CC": ["gallon - $240.00 (USD)"],
}



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
        self.open_link(f'shop.perfumersapprentice.com/c-84-bulk-sizes.aspx?pagenum={1}')
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
                    text = price.text

                    prefix = price.text[0:4]

                    if 'gall' in prefix:
                        spisok.append(text)

                    elif prefix == 'case':
                        spisok.append(text.replace(' (4) 2week lead time', ''))

                    elif prefix == 'doub':
                        spisok.append(text.replace(' (8) 2 week lead time',''))
                    if len(spisok) > 0:
                        self.log.info(f'FOR {aroma_name} added value : {spisok}')

                if len(spisok) > 0:
                    names_list.update({aroma_name: spisok})
            self.log.info('-----------------------')
            self.log.info(names_list)

    def count_find_elements2(self):
        global names_list, data, aroma_name
        self.open_link(f'shop.perfumersapprentice.com/c-84-bulk-sizes.aspx?pagenum={2}')
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
                    text = price.text
                    prefix = price.text[0:4]

                    if 'gall' in prefix:
                        spisok.append(price.text)

                    elif prefix == 'case':
                        spisok.append(text.replace(' (4) 2week lead time', ''))

                    elif prefix == 'doub':
                        spisok.append(text.replace('(8) 2 week lead time',''))
                    if len(spisok) > 0:
                        self.log.info(f'FOR {aroma_name} added value : {spisok}')

                if len(spisok) > 0:
                    names_list.update({aroma_name: spisok})
            self.log.info('-----------------------')
            self.log.info(names_list)

    def count_find_elements3(self):
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
                    text = price.text

                    prefix = price.text[0:4]

                    if 'gall' in prefix:
                        spisok.append(price.text)

                    elif prefix == 'case':
                        spisok.append(text.replace('case (4) 2week lead time', ''))

                    elif prefix == 'doub':
                        spisok.append(text.replace('(8) 2 week lead time',''))
                    if len(spisok) > 0:
                        self.log.info(f'FOR {aroma_name} added value : {spisok}')

                if len(spisok) > 0:
                    names_list.update({aroma_name: spisok})
            self.log.info('-----------------------')
            self.log.info(names_list)

    def compare_dicts(self):
        self.log.info("start compare")
        global data ,names_list
        added, removed, modified, same = dict_compare(names_list, data)
        for products, prises_list in modified.items():
            arr = prises_list[0]
            arr2 = prises_list[1]
            i = 0
            if len(arr) == len(arr2):
                while i < len(arr):
                    self.log.info(f'arr1 = {arr}')
                    self.log.info(f'arr2 = {arr2}')
                    if arr[i] != arr2[i]:
                        self.log.info(f" {products} \nOLD  {arr2[i]} \nNEW {arr[i]}")

                        i += 1
                    else:
                        i += 1
            else:
                self.log.info(f'New position was added/removed \n\nOld file:\n{products}  {arr2} '
                      f'\n\nNew file: \n{products}  {arr}')

            for key, value in names_list.items():
                print(key)
                print(value)
