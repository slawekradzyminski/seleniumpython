from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_searching_in_duckduckgo():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony duckduckgo
    browser.get('https://www.duckduckgo.com')

    # Znalezienie paska wyszukiwania
    searchbar = browser.find_element(By.ID, 'search_form_input_homepage')

    # Znalezienie guzika wyszukiwania (lupki)
    search_button = browser.find_element(By.ID, 'search_button_homepage')

    # Asercje że elementy są widoczne dla użytkownika
    assert searchbar.is_displayed() is True
    assert search_button.is_displayed() is True

    # Szukanie Vistula University
    searchbar.send_keys('Vistula University')
    search_button.click()

    # Sprawdzenie że pierwszy wynik ma tytuł 'Vistula University in Warsaw'
    listOfTitles = browser.find_elements(By.CLASS_NAME, 'result__title')
    assert listOfTitles[1].text == 'Vistula University in Warsaw'

    # Zamknięcie przeglądarki
    browser.quit()

