import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def test_searching_in_google():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.set_window_size(1920, 1080)

    # Otwarcie strony duckduckgo
    browser.get('https://google.com')

    # Znalezienie paska wyszukiwania
    cookie_accept = browser.find_element(By.CSS_SELECTOR, '#L2AGLb div')

    cookie_accept.click()
    # Znalezienie guzika wyszukiwania (lupki)
    # search_button = browser.find_element(By.CSS_SELECTOR, '[aria-label=Search]')
    #
    # # Asercje że elementy są widoczne dla użytkownika
    # assert search_input.is_displayed() is True
    # assert search_button.is_displayed() is True
    #
    # # Szukanie 4testers
    # search_input.send_keys('4testers')
    # search_button.click()
    #
    # # Sprawdzenie że jakikolwiek wynik ma tytuł '4testers'
    # # lista Seleniumowych WebElementów które reprezentują nam tytuły stron
    #
    # wait = WebDriverWait(browser, 10)
    # element_to_wait_for = (By.CSS_SELECTOR, 'h2 a')
    # wait.until(expected_conditions.visibility_of_element_located(element_to_wait_for))
    #
    # results = browser.find_elements(By.CSS_SELECTOR, 'h2 a')
    #
    # # lista tytułów (stringów)
    # list_of_titles = []
    # for i in results:
    #     list_of_titles.append(i.text)
    #
    # # asercja
    # assert '4_testers - nowy kurs dla testerów oprogramowania' in list_of_titles
    #
    # # Zamknięcie przeglądarki
    browser.quit()

