from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# Test - uruchomienie Chroma
def test_my_first_chrome_selenium_test():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony testareny - pierwsze użycie Selenium API
    browser.get('http://demo.testarena.pl/zaloguj')

    # Weryfikacja czy tytuł otwartej strony zawiera w sobie 'TestArena'
    assert browser.title.__contains__('TestArena')

    # Zamknięcie przeglądarki
    browser.quit()


# Test - uruchomienie Firefoxa
def test_my_first_firefox_selenium_test():
    zadanie = "Dla Was"

    # Uruchomienie przeglądarki Firefox. Ścieżka do geckodrivera (drivera dla Firefoxa)
    # ustawiana automatycznie przez bibliotekę webdriver-manager

    # Otwarcie strony testareny - pierwsze użycie Selenium API

    # Weryfikacja czy tytuł otwartej strony zawiera w sobie 'TestArena'

    # Zamknięcie przeglądarki
