import time

from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def test_searching_in_bing():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.set_window_size(1920, 1080)

    # Otwarcie strony duckduckgo
    browser.get('https://bing.com')

    # Akceptacja ciastka
    wait = WebDriverWait(browser, 10)
    element_to_wait_for = (By.ID, 'bnp_btn_accept')
    wait.until(expected_conditions.visibility_of_element_located(element_to_wait_for))
    browser.find_element(By.ID, 'bnp_btn_accept').click()

    # Znalezienie paska wyszukiwania
    search_input = browser.find_element(By.CSS_SELECTOR, '#sb_form_q')

    # Asercje że elementy są widoczne dla użytkownika
    assert search_input.is_displayed() is True

    # Szukanie 4testers
    search_input.send_keys('4testers' + Keys.ENTER)

    # Sprawdzenie że jakikolwiek wynik ma tytuł '4testers'
    # lista Seleniumowych WebElementów które reprezentują nam tytuły stron

    element_to_wait_for = (By.CSS_SELECTOR, 'h2 a')
    wait.until(expected_conditions.visibility_of_element_located(element_to_wait_for))

    results = browser.find_elements(By.CSS_SELECTOR, 'h2 a')

    # lista tytułów (stringów)
    list_of_titles = []
    for i in results:
        list_of_titles.append(i.text)

    # asercja
    assert '4_testers – nowy kurs dla testerów oprogramowania' in list_of_titles

    # Zamknięcie przeglądarki
    browser.quit()

