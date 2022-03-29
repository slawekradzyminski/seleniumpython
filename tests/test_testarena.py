import time

import pytest
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import config
import string
import random

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


@pytest.fixture()
def browser():
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.get('http://demo.testarena.pl/zaloguj')
    yield browser
    browser.quit()


def test_login_successfully(browser):
    login_page = LoginPage(browser)
    login_page.login(config.login, config.password)
    home_page = HomePage(browser)
    home_page.wait_for_load()


def test_logout_successfully(browser):
    login_page = LoginPage(browser)
    login_page.login(config.login, config.password)
    home_page = HomePage(browser)
    home_page.logout()

    assert browser.find_element(By.CLASS_NAME, 'login_avatar').is_displayed()


def test_open_user_profile(browser):
    login_page = LoginPage(browser)
    login_page.login(get_random_string(10), config.password)
    home_page = HomePage(browser)
    home_page.wait_for_load()
    home_page.go_to_user_profile()
    profile_page = ProfilePage(browser)
    profile_page.verify_email(config.login)

    project_name = get_random_string(10)
    browser.find_element(By.ID, 'name').send_keys(project_name)

    browser.find_element(By.ID, 'search').send_keys(project_name)


def get_random_string(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
