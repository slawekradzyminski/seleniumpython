import time

from selenium.webdriver import Chrome
from selenium.webdriver import Edge
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager


# Test - uruchomienie Chroma
def test_my_first_chrome_selenium_test():
    # Setup drivera. Driver jest pobierany automatycznie przez bibliotekę webdriver-manager
    service = Service(ChromeDriverManager().install())
    # Uruchomienie przeglądarki
    browser = Chrome(service=service)
    browser.set_window_size(1920, 1080)

    # Otwarcie strony testareny - pierwsze użycie Selenium API
    browser.get('http://demo.testarena.pl/zaloguj')

    # Weryfikacja czy tytuł otwartej strony zawiera w sobie 'TestArena'
    assert 'TestArena' in browser.title

    # Zamknięcie przeglądarki
    time.sleep(4)
    browser.quit()


def test_awesome_testing():
    # Setup drivera. Driver jest pobierany automatycznie przez bibliotekę webdriver-manager
    service = Service(ChromeDriverManager().install())
    # Uruchomienie przeglądarki
    browser = Chrome(service=service)
    browser.set_window_size(1920, 1080)

    # Otwarcie strony testareny - pierwsze użycie Selenium API
    browser.get('https://awesome-testing.blogspot.com/')

    # Zeby dodac ciastko musimy najpierw wejść na daną stronę
    browser.add_cookie({"name": "displayCookieNotice", "value": "y"})
    browser.refresh()

    # Weryfikacja czy tytuł otwartej strony zawiera w sobie 'TestArena'
    assert browser.title == 'Software testing Blog - Awesome Testing'

    # Zamknięcie przeglądarki
    time.sleep(3)
    browser.quit()


# Test - uruchomienie Edge
def test_my_first_edge_selenium_test():
    # Uruchomienie przeglądarki Edge. Ścieżka do geckodrivera (drivera dla Firefoxa)
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    service = Service(EdgeChromiumDriverManager().install())
    browser = Edge(service=service)


    # Otwarcie strony www.google.pl

    # Weryfikacja tytułu

    # Zamknięcie przeglądarki
    browser.quit()
