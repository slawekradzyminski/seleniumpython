from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_searching_in_duckduckgo():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony duckduckgo
    browser.get('https://duckduckgo.com')

    # Znalezienie paska wyszukiwania
    search_bar = browser.find_element(By.ID, 'search_form_input_homepage')

    # Znalezienie guzika wyszukiwania (lupki)
    search_button = browser.find_element(By.ID, 'search_button_homepage')

    # Asercje że elementy są widoczne dla użytkownika
    assert search_bar.is_displayed() is True
    assert search_button.is_displayed() is True

    # Szukanie Vistula University
    search_bar.send_keys('Vistula University')
    search_button.click()

    # Sprawdzenie że chociaż jeden wynik ma tytuł 'Vistula University in Warsaw'
    result_titles = browser.find_elements(By.CLASS_NAME, 'result__title')
    list_of_titles = []
    for i in result_titles:
        list_of_titles.append(i.text)
    assert 'Vistula University in Warsaw' in list_of_titles

    # Zamknięcie przeglądarki
    browser.quit()


def test_searching_in_bing():
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.get('https://www.bing.com')

    # Znalezienie paska wyszukiwania
    search_bar = browser.find_element(By.ID, 'sb_form_q')

    # Znalezienie guzika wyszukiwania (lupki)
    search_button = browser.find_element(By.CSS_SELECTOR, '#search_icon')

    # Asercje że elementy są widoczne dla użytkownika
    assert search_bar.is_displayed() is True
    assert search_button.is_displayed() is True

    # Szukanie Vistula University
    search_bar.send_keys('Vistula University')
    search_button.click()

    # Sprawdzenie że chociaż jeden wynik ma tytuł 'Vistula University in Warsaw'
    result_titles = browser.find_elements(By.CSS_SELECTOR, '.b_algo h2')
    list_of_titles = []
    for i in result_titles:
        list_of_titles.append(i.text)
    assert 'Vistula University in Warsaw' in list_of_titles

    # Zamknięcie przeglądarki
    browser.quit()