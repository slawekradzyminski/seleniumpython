from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def test_searching_in_duckduckgo():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    service = Service(ChromeDriverManager().install())
    browser = Chrome(service=service)
    browser.set_window_size(1920, 1080)

    # Otwarcie strony duckduckgo
    browser.get('https://www.duckduckgo.com')

    browser.find_element(By.CSS_SELECTOR, '#searchbox_input').send_keys('4testers')
    browser.find_element(By.CSS_SELECTOR, '[aria-label=Search]').click()

    # Sprawdzenie że pierwszy element ma w sobie tytuł '4_testers - Kurs Tester Oprogramowania'
    # Tutaj musimy zaczekać aż tytuły się załadują
    wait = WebDriverWait(browser, timeout=10, poll_frequency=0.2)
    # Pythonowa tupla / krotki
    result_title = (By.CSS_SELECTOR, '[data-testid=result-title-a] span')
    wait.until(expected_conditions.presence_of_all_elements_located(result_title))

    titles = browser.find_elements(By.CSS_SELECTOR, '[data-testid=result-title-a] span')
    assert '4_testers Automaty - Kurs Tester Automatyzujący & AI' in titles[0].text

    # Zamknięcie przeglądarki
    browser.quit()

