from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# Test - uruchomienie Chroma
def test_my_first_chrome_selenium_test():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    # To jest nasz komentarz i on nie ma żadnego wpływu na nasz kod
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony testareny - pierwsze użycie Selenium API
    browser.get('http://demo.testarena.pl/zaloguj')

    # Weryfikacja czy tytuł otwartej strony zawiera w sobie 'TestArena'
    assert 'TestArena' in browser.title
    assert browser.current_url == 'http://demo.testarena.pl/zaloguj'

    # Zamknięcie przeglądarki
    browser.quit()


def test_login():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    # To jest nasz komentarz i on nie ma żadnego wpływu na nasz kod
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony testareny - pierwsze użycie Selenium API
    browser.get('http://demo.testarena.pl/zaloguj')

    # Wpisanie login, hasła i kliknięcie login
    browser.find_element(By.CSS_SELECTOR, "#email").send_keys("administrator@testarena.pl")
    browser.find_element(By.CSS_SELECTOR, "#password").send_keys("sumXQQ72$L")
    browser.find_element(By.CSS_SELECTOR, "#login").click()

    # Przykładowa asercja - sprawdzenie że na stronie jest jakiś selektor który wyświetla
    # się tylko w przypadku udanego logowania
    assert browser.find_element(By.CSS_SELECTOR, '[title=Wyloguj]').is_displayed() is True

    # Zamknięcie przeglądarki
    time.sleep(2)
    browser.quit()


def test_login_with_elements_as_objects():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony testareny - pierwsze użycie Selenium API
    browser.get('http://demo.testarena.pl/zaloguj')

    # Stworzenie obiektów reprezentujących elementy strony
    email_input = browser.find_element(By.CSS_SELECTOR, "#email")
    password_input = browser.find_element(By.CSS_SELECTOR, "#password")
    login_button = browser.find_element(By.CSS_SELECTOR, "#login")

    # Wpisanie login, hasła i kliknięcie login
    email_input.send_keys("administrator@testarena.pl")
    password_input.send_keys("sumXQQ72$L")
    login_button.click()

    # Przykładowa asercja - sprawdzenie że na stronie jest jakiś selektor który wyświetla
    # się tylko w przypadku udanego logowania
    log_out_button = browser.find_element(By.CSS_SELECTOR, '[title=Wyloguj]')
    assert log_out_button.is_displayed() is True

    # Zamknięcie przeglądarki
    time.sleep(1)
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
