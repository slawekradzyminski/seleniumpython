from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_searching_in_duckduckgo():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony duckduckgo
    browser.get('https://duckduckgo.com')
    # Znalezienie paska wyszukiwania

    # Znalezienie guzika wyszukiwania (lupki)

    # Asercje że elementy są widoczne dla użytkownika

    # Szukanie Vistula University

    # Sprawdzenie że pierwszy wynik ma tytuł 'Vistula University in Warsaw'

    # Zamknięcie przeglądarki

