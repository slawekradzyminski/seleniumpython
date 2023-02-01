import time

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser():
    # Faza 1 - coś co się wykona przed każdym testem
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.get('https://www.awesome-testing.com')

    # Faza 2 - coś co przekazujemy do każdego testu
    yield browser

    # Faza 3 - coś co się wykona po każdym teście
    browser.quit()


def test_post_count(browser):
    # Pobranie listy tytułów
    titles = browser.find_elements(By.CSS_SELECTOR, '.post-title')

    # Asercja że lista ma 4 elementy
    assert len(titles) == 4


def test_post_count_after_search(browser):
    # Inicjalizacja searchbara i przycisku search
    search_bar = browser.find_element(By.CSS_SELECTOR, 'input.gsc-input')
    search_button = browser.find_element(By.CSS_SELECTOR, '.gsc-search-button')

    # Szukanie
    search_bar.send_keys('cypress')
    search_button.click()

    # Pobranie listy tytułów
    titles = browser.find_elements(By.CSS_SELECTOR, '.post-title')

    # Asercja że lista ma 5 elementów
    assert len(titles) == 5


def test_post_count_on_cypress_label(browser):
    # Inicjalizacja elementu z labelką
    cypress_label = browser.find_element(By.LINK_TEXT, 'Cypress')

    # Kliknięcie na labelkę
    cypress_label.click()

    # Pobranie listy tytułów
    titles = browser.find_elements(By.CSS_SELECTOR, '.post-title')

    # Asercja że lista ma 1 element
    assert len(titles) == 1
