import time

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions

from pages.arena.home_page import HomePage
from pages.arena.login_page import LoginPage
from pages.arena.project_page import ProjectPage

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
    home_page = HomePage(browser)
    home_page.click_logout()

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
    home_page = HomePage(browser)
    home_page.click_on_administrator_link()

    project_page = ProjectPage(browser)
    project_page.search_for_project('kamil')
    project_page.verify_projects_found('kamil')
