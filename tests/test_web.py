from selenium.webdriver import Chrome
from selenium.webdriver import Edge
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time


# Test - uruchomienie Chroma
def test_my_first_chrome_selenium_test():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony testareny - pierwsze użycie Selenium API
    browser.get('http://demo.testarena.pl/zaloguj')

    # Weryfikacja czy tytuł otwartej strony zawiera w sobie 'TestArena'
    assert 'TestArena' in browser.title

    # Zamknięcie przeglądarki
    browser.quit()


# Test - uruchomienie Firefoxa
def test_my_first_firefox_selenium_test():
    # Uruchomienie przeglądarki Firefox. Ścieżka do geckodrivera (drivera dla Firefoxa)
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Edge(executable_path=EdgeChromiumDriverManager().install())

    # Otwarcie strony www.google.pl
    browser.get('https://www.google.pl')
    browser.set_window_size(1280, 720)

    # Weryfikacja tytułu
    assert 'Google' in browser.title

    # Sztuczne czekanie na potrzeby szkolenia
    time.sleep(5)

    # Zamknięcie przeglądarki
    browser.quit()
