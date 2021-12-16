import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help='Choose browser: chrome or firefox')
    parser.addoption('--language',
                     action='store',
                     default=None,
                     help='Choose language: ru, es, fr')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs',
                                    {'intl.accept_languages': user_language})
    if browser_name == 'chrome':
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        browser = webdriver.Firefox(options=options)
    yield browser
    browser.quit()
