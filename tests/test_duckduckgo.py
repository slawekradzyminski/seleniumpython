from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def test_searching_in_duckduckgo():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony duckduckgo

    # Znalezienie paska przeglądarki

    # Znalezienie guzika wyszukiwania (lupki)

    # Asercje że elementy są widoczne dla użytkownika

    #Szukanie Vistula University

    #Sprawdź że pierwszy wynik ma tytuł 'Vistula University in Warsaw'

    # Zamknięcie przeglądarki
