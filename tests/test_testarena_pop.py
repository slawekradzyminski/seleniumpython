import time

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions

from pages.arena.login_page import LoginPage

administrator_email = 'administrator@testarena.pl'


@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    browser = Chrome(service=service)
    browser.set_window_size(1920, 1080)
    login_page = LoginPage(browser)
    login_page.visit()
    login_page.login(administrator_email, 'sumXQQ72$L')

    yield browser
    browser.quit()


def test_testarena_login(browser):
    user_email = browser.find_element(By.CSS_SELECTOR, '.user-info small').text
    assert user_email == administrator_email


def test_logout(browser):
    browser.find_element(By.CSS_SELECTOR, '.icons-switch').click()

    assert '/zaloguj' in browser.current_url
    assert browser.find_element(By.CSS_SELECTOR, '#password').is_displayed()


def test_add_message(browser):
    browser.find_element(By.CSS_SELECTOR, '.top_messages').click()
    # zło
    # time.sleep(8)
    # zamiast tego czekamy aż element będzie miał określony stan
    # konstruktor przyjmuje 2 parametry, nasz obiekt przeglądarki/drivera i maksymalny czas czekania
    wait = WebDriverWait(browser, 10)
    # Pythonowa tupla / krotki
    message_area = (By.CSS_SELECTOR, '#j_msgContent')
    wait.until(expected_conditions.element_to_be_clickable(message_area))

    browser.find_element(By.CSS_SELECTOR, '#j_msgContent').send_keys('Wiadomość')


def test_search_for_project(browser):
    browser.find_element(By.CSS_SELECTOR, '.header_admin a').click()
    browser.find_element(By.CSS_SELECTOR, '#search').send_keys('Kamil')
    browser.find_element(By.CSS_SELECTOR, '#j_searchButton').click()

    found_projects = browser.find_elements(By.CSS_SELECTOR, 'tbody tr')
    assert len(found_projects) > 0

    names = browser.find_elements(By.CSS_SELECTOR, 'tbody tr td:nth-of-type(1)')
    for name in names:
        assert 'kamil' in name.text.lower()
