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

    # Otwarcie strony

    # Pobranie listy tytułów

    # Asercja że lista ma 4 elementy

    # Zamknięcie przeglądarki


def test_post_count_after_search():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony

    # Inicjalizacja searchbara i przycisku search

    # Szukanie

    # Czekanie na stronę

    # Pobranie listy tytułów

    # Asercja że lista ma 3 elementy

    # Zamknięcie przeglądarki


def test_post_count_on_cypress_label():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony

    # Inicjalizacja elementu z labelką

    # Kliknięcie na labelkę

    # Czekanie na stronę

    # Pobranie listy tytułów

    # Asercja że lista ma 1 element

    # Zamknięcie przeglądarki
