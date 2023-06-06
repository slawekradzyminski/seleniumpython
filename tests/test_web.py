import time

from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# Test - uruchomienie Chroma
def test_my_first_chrome_selenium_test():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony testareny - pierwsze użycie Selenium API
    browser.get('http://demo.testarena.pl/zaloguj')

    # Sprawiamy żeby przeglądarka była na całym ekranie
    browser.maximize_window()

    # Weryfikacja czy tytuł otwartej strony zawiera w sobie 'TestArena'
    assert 'TestArena' in browser.title

    # Zamknięcie przeglądarki
    time.sleep(3)
    browser.quit()


def test_should_open_duckduckgo_com():
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony testareny - pierwsze użycie Selenium API
    browser.get('https://duckduckgo.com')

    # Sprawiamy żeby przeglądarka była na całym ekranie
    browser.set_window_size(1024, 768)

    # Weryfikacja czy tytuł otwartej strony zawiera w sobie 'TestArena'
    assert 'DuckDuckGo' in browser.title

    # Zamknięcie przeglądarki
    time.sleep(3)
    browser.quit()


# Test - uruchomienie Firefoxa
def test_my_first_firefox_selenium_test():
    # Uruchomienie przeglądarki Firefox. Ścieżka do geckodrivera (drivera dla Firefoxa)
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Firefox(executable_path=GeckoDriverManager().install())


    # Otwarcie strony www.google.pl

    # Weryfikacja tytułu

    # Zamknięcie przeglądarki
    browser.quit()
