from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: rus or es")
    
\
@pytest.fixture(scope="function")
def browser():
    # language = request.config.getoption("language")
    # browser = None
    # options = Options()
    # options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(
        # options=options
        )
    
    yield browser
    print("\nquit browser..")
    browser.quit()


