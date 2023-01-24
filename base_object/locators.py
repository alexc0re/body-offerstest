from selenium.webdriver.common.by import By


class AbusePageLocators:
    AROMA_BLOCK = (By.CSS_SELECTOR, '.equal-rows')
    AROMA_NAME = (By.CSS_SELECTOR, '.equal-rows h2')
    PRICE = (By.CSS_SELECTOR, '.product-variants li')
