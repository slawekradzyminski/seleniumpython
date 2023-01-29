import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_searching_in_bing():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    chrome_options = Options()
    options = [
        "--headless",
        "--disable-gpu",
        "--window-size=1920,1200",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage"
    ]
    for option in options:
        chrome_options.add_argument(option)
    browser = Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

    # Otwarcie strony bing
    browser.get('https://bing.com')

    # Znalezienie paska wyszukiwania
    search_input = browser.find_element(By.CSS_SELECTOR, "#sb_form_q")

    # Znalezienie guzika wyszukiwania (lupki)
    search_button = browser.find_element(By.CSS_SELECTOR, "#search_icon")

    # Asercje że elementy są widoczne dla użytkownika
    assert search_input.is_displayed() is True
    assert search_button.is_displayed() is True

    # Szukanie Vistula University
    search_input.send_keys('Vistula University')
    search_button.click()

    # Sprawdzenie że lista wyników jest dłuższa niż 2
    search_results = browser.find_elements(By.CSS_SELECTOR, '.b_algo')
    assert len(search_results) > 2

    ## Sprawdzenie że pierwszy element to strona uczelni
    # titles = browser.find_elements(By.CSS_SELECTOR, '.b_topTitle')
    # first_title_text = titles[0].text
    # assert first_title_text == 'Home - Vistula University'

    # Zamknięcie przeglądarki
    time.sleep(1)
    browser.quit()

