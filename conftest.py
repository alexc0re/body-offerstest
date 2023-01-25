import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import AbusePage
options = Options()


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',  # Browser Language selection
                     help="Choose language: en or es")

    parser.addoption('--browsermode', action='store', default='start-maximized',  # Browser mode selection
                     help="--headless mode")




@pytest.fixture(scope="session")
def driver(request):
    driver_mode = request.config.getoption('browsermode')
    driver_lang = request.config.getoption("language")
    print(f"\nstart {driver_lang} chrome browser with {driver_mode} parameter")
    options.add_argument(driver_mode)
    options.add_experimental_option('prefs', {'intl.accept_languages': driver_lang})
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    yield driver
    print("\nquit browser..")
    driver.quit()



@pytest.fixture
def abuse_page(driver):
    yield AbusePage(driver)
