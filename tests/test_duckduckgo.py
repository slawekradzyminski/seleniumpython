import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# def test_searching_in_duckduckgo():
#     # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
#     # ustawiana automatycznie przez bibliotekę webdriver-manager
#     browser = Chrome(executable_path=ChromeDriverManager().install())
#     browser.set_window_size(1720, 1280)
#
#     # Otwarcie strony duckduckgo
#     browser.get('https://duckduckgo.com')
#
#     # Znalezienie paska wyszukiwania
#     search_input = browser.find_element(By.CSS_SELECTOR, "#searchbox_input")
#
#     # Znalezienie guzika wyszukiwania (lupki)
#     search_button = browser.find_element(By.CSS_SELECTOR, "[aria-label=Search]")
#
#     # Asercje że elementy są widoczne dla użytkownika
#     assert search_input.is_displayed() is True
#     assert search_button.is_displayed() is True
#
#     # Szukanie Vistula University
#     search_input.send_keys('Vistula University')
#     search_button.click()
#
#     # Sprawdzenie że lista wyników jest dłuższa niż 2
#     search_results = browser.find_elements(By.CSS_SELECTOR, '.nrn-react-div')
#     assert len(search_results) > 2
#
#     ## Sprawdzenie że pierwszy element to strona uczelni
#     first_result = browser.find_element(By.CSS_SELECTOR, '#r1-0 h2 span')
#     text_inside_element = first_result.text
#     assert text_inside_element == 'Home - Vistula University'
#
#     # Zamknięcie przeglądarki
#     time.sleep(1)
#     browser.quit()

