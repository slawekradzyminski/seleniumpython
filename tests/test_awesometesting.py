import pytest
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_post_count():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony awesome-testing.com
    browser.get("https://awesome-testing.com")

    # Pobranie listy tytułów
    titles = browser.find_elements(By.CSS_SELECTOR, '.post-title')

    # Asercja że lista ma 4 elementy
    assert len(titles) == 4

    # Zamknięcie przeglądarki
    browser.quit()


def test_post_count_after_search():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony
    browser.get("https://awesome-testing.com")

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

    # Zamknięcie przeglądarki
    browser.quit()


def test_post_count_on_cypress_label():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony
    browser.get('https://www.awesome-testing.com')

    # Inicjalizacja elementu z labelką
    cypress_label = browser.find_element(By.LINK_TEXT, 'Cypress')

    # Kliknięcie na labelkę
    cypress_label.click()

    # Pobranie listy tytułów
    titles = browser.find_elements(By.CSS_SELECTOR, '.post-title')

    # Asercja że lista ma 1 element
    assert len(titles) == 1

    # Zamknięcie przeglądarki
    browser.quit()
