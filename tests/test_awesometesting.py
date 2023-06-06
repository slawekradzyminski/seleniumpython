import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture()
def browser():
    # 1 - To wykona się PRZED każdym testem który korzysta z tego fixture'a
    driver = Chrome(executable_path=ChromeDriverManager().install())
    driver.get('https://awesome-testing.blogspot.com')
    # 2 - To jest to co zwracamy (przekazujemy) do testów
    yield driver
    # 3 - To wykona się PO każdym teście który korzysta z tego fixture'a
    driver.quit()


def test_post_count(browser):
    titles = browser.find_elements(By.CSS_SELECTOR, '.post-title')
    assert len(titles) == 4


def test_post_count_after_search(browser):
    # Inicjalizacja searchbara i przycisku search
    search_bar = browser.find_element(By.CSS_SELECTOR, 'input.gsc-input')
    search_button = browser.find_element(By.CSS_SELECTOR, 'input.gsc-search-button')

    # Szukanie
    search_bar.send_keys('selenium')
    search_button.click()

    # Czekanie na stronę
    wait = WebDriverWait(browser, 10)
    element_to_wait_for = (By.CSS_SELECTOR, '.status-msg-body')
    wait.until(expected_conditions.visibility_of_element_located(element_to_wait_for))

    # Pobranie listy tytułów/postów
    titles = browser.find_elements(By.CSS_SELECTOR, '.post-title')

    # Asercja że lista ma 20 elementów
    assert len(titles) == 20


def test_post_count_on_2016_label(browser):
    # Inicjalizacja elementu z labelką 2016
    label_2016 = browser.find_element(By.LINK_TEXT, '2016')

    # Kliknięcie na labelkę 2016
    label_2016.click()

    # Pobranie listy tytułów/postów
    titles = browser.find_elements(By.CSS_SELECTOR, '.post-title')

    # Asercja że lista ma 24 elementy
    assert len(titles) == 24
