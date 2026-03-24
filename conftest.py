import pytest
from selenium import webdriver

@pytest.fixture
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()      # pytest -v -s testCases/test_login.py --browser chrome
    elif browser=='firefox':
        driver = webdriver.Firefox()     # pytest -v -s testCases/test_login.py --browser firefox
    else:
        driver = webdriver.Ie()          # default
    return driver


def pytest_addoption(parser):     # this will get the value from command line / hooks
    parser.addoption("--browser")


@pytest.fixture
def browser(request):            # this will return the browser value to setup method
    return request.config.getoption("--browser")



########### PyTest HTML Reports  ###################

# hook for adding environment info to html report

def pytest_configure(config):
    if hasattr(config, '_metadata'):
        config._metadata['Project Name'] = 'nopcommerce'
        config._metadata['Module Name'] = 'Customers'
        config._metadata['Tester'] = 'Shubham'


# hook for delete/modify environment info to html report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME',None)
    metadata.pop('Plugins',None)