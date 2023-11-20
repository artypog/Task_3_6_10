import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", \
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None, \
                     help="Choose language: Russian(ru), English(en), French(fr) etc.")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    language = language.lower() + '-' + language.upper() + ', ' + language.lower()
    browser = None
    if browser_name == "chrome":
        print(f"\nstart chrome browser for test language = {language}..")
        chromeoptions = chromeOptions()
        chromeoptions.add_experimental_option('prefs', {'intl.accept_languages': language})

        browser = webdriver.Chrome(options=chromeoptions)
    elif browser_name == "firefox":
        print(f"\nstart firefox browser for test language = {language}..")
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.binary_location = language
        browser = webdriver.Firefox(options=firefox_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
