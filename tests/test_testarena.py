import pytest
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import config

login = 'administrator@testarena.pl'
password = 'sumXQQ72$L'


@pytest.fixture()
def browser():
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.get('http://demo.testarena.pl/zaloguj')
    yield browser
    browser.quit()


def test_login_successfully(browser):
    browser.find_element(By.ID, 'email').send_keys(config.login)
    browser.find_element(By.ID, 'password').send_keys(config.password)
    browser.find_element(By.ID, 'login').click()

    wait = WebDriverWait(browser, 10)
    grey_bar = (By.LINK_TEXT, 'Kokpit')
    wait.until(expected_conditions.presence_of_element_located(grey_bar))

