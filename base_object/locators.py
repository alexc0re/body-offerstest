from selenium.webdriver.common.by import By


class AbusePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#ctl00_lnkSignInOut')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#ctl00_PageContent_ctl00_ctrlLogin_UserName')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#ctl00_PageContent_ctl00_ctrlLogin_Password')
    LOGIN_BTN = (By.CSS_SELECTOR, '#ctl00_PageContent_ctl00_ctrlLogin_LoginButton')
    AROMA_BLOCK = (By.CSS_SELECTOR, '.equal-rows')
    AROMA_NAME = (By.CSS_SELECTOR, '.equal-rows h2')
    PRICE = (By.CSS_SELECTOR, '.product-variants li')

