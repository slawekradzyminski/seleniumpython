import pytest
from selenium.webdriver import Chrome
import json

DEFAULT_WAIT_TIME = 10
CONFIG_PATH = './config.json'


@pytest.fixture(scope='session')
def config():
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def config_wait_time(config):
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture
def browser(config, config_wait_time):
    # Initialize Driver or raise exception
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    if 'chrome' not in config['browser']:
        raise Exception('Only chrome is supported right now"')
    if config['browser'] == 'chrome':
        driver = Chrome()
    else:
        raise Exception(f'"{config["browser"]}" is not a supported browser')

    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(config_wait_time)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()