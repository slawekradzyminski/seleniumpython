import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages.cockpit_page import CockpitPage
from pages.login_page import LoginPage
from pages.panel_page import PanelPage


@pytest.fixture()
def browser():
    browser = Chrome(executable_path=ChromeDriverManager().install())
    # stworzenie obiektu klasy (page objectu) LoginPage'a
    login_page = LoginPage(browser)
    # wywołanie metod na obiekcie klasy
    login_page.load()
    login_page.login("administrator@testarena.pl", "sumXQQ72$L")
    yield browser
    browser.quit()


def test_logout_correctly_displayed(browser):
    assert browser.find_element(By.CSS_SELECTOR, '[title=Wyloguj]').is_displayed() is True


def test_opens_messages(browser):
    cockpit_page = CockpitPage(browser)
    cockpit_page.click_envelope()

    panel_page = PanelPage(browser)
    panel_with_messages = panel_page.wait_for_load()
    assert panel_with_messages.is_displayed()


def test_open_administration(browser):
    cockpit_page = CockpitPage(browser)
    cockpit_page.click_administration()

    assert browser.find_element(By.CSS_SELECTOR, '.content_title').text == 'Projekty'