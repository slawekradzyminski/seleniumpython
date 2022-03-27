import pytest
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture()
def browser():
    # Sekcja 1 - wykona się przed każdym testem
    options = webdriver.ChromeOptions()
    options.add_argument('--start-fullscreen')
    browser = Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
    browser.get('https://www.awesome-testing.com')
    # Sekcja 2 - zwracamy przeglądarkę (webdrivera) dzięki czemu nie musimy go tworzyć za każdym razem
    yield browser
    # Sekcja 3 - wykona się po każdym teście
    browser.quit()


def test_post_count(browser):
    titles = browser.find_elements(By.CLASS_NAME, 'post-title')
    assert len(titles) == 4


def test_post_count_after_search(browser):
    # Inicjalizacja searchbara i przycisku search
    search_bar = browser.find_element(By.CSS_SELECTOR, 'input.gsc-input')
    search_button = browser.find_element(By.CSS_SELECTOR, 'input.gsc-search-button')

    # Szukanie
    search_bar.send_keys('Cypress')
    search_button.click()

    # Czekanie na stronę
    wait = WebDriverWait(browser, 10)
    grey_bar = (By.CLASS_NAME, 'status-msg-body')
    wait.until(expected_conditions.presence_of_element_located(grey_bar))

    # Pobranie listy tytułów
    titles = browser.find_elements(By.CLASS_NAME, 'post-title')

    # Asercja że lista ma 4 elementy
    assert len(titles) == 4


def test_post_count_on_cypress_label(browser):
    # Inicjalizacja elementu z labelką
    cypress_label = browser.find_element(By.LINK_TEXT, 'Cypress')

    # Kliknięcie na labelkę
    cypress_label.click()

    # Czekanie na stronę
    wait = WebDriverWait(browser, 10)
    grey_bar = (By.CLASS_NAME, 'status-msg-body')
    wait.until(expected_conditions.presence_of_element_located(grey_bar))

    # Pobranie listy tytułów
    titles = browser.find_elements(By.CLASS_NAME, 'post-title')

    # Asercja że lista ma 4 elementy
    assert len(titles) == 1


def test_social_links(browser):
    social_links = browser.find_elements(By.CSS_SELECTOR, '#HTML1 a')
    assert social_links[0].get_attribute('href') == 'https://www.facebook.com/AwesomeTestingBlog'
    assert social_links[1].get_attribute('href') == 'https://twitter.com/s_radzyminski'
