from selenium.webdriver import Chrome
from selenium.webdriver import Edge
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager

# Test - uruchomienie Chroma
def test_my_first_chrome_selenium_test():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    service = Service(ChromeDriverManager().install())
    browser = Chrome(service=service)

    # Otwarcie strony testareny - pierwsze użycie Selenium API
    browser.get('http://demo.testarena.pl/zaloguj')

    # Weryfikacja czy tytuł otwartej strony zawiera w sobie 'TestArena'
    assert 'TestArena' in browser.title

    # Zamknięcie przeglądarki
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
