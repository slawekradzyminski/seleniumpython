import re

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_post_count():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    service = Service(ChromeDriverManager().install())
    browser = Chrome(service=service)
    browser.set_window_size(1920, 1080)

    # Otwarcie strony
    browser.get('http://www.awesome-testing.blogspot.com')

    # Pobranie listy tytułów
    posts = browser.find_elements(By.CSS_SELECTOR, '.post-title')

    # Asercja że lista ma 4 elementy
    assert len(posts) == 4

    # Zamknięcie przeglądarki
    browser.quit()


def test_post_count_after_search():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    service = Service(ChromeDriverManager().install())
    browser = Chrome(service=service)
    browser.set_window_size(1920, 1080)

    # Otwarcie strony
    browser.get('http://www.awesome-testing.blogspot.com')

    # Szukanie
    browser.find_element(By.CSS_SELECTOR, '.gsc-input input').send_keys('Selenium')
    browser.find_element(By.CSS_SELECTOR, '.gsc-search-button input').click()

    # Czekanie na stronę

    # Pobranie listy tytułów
    posts = browser.find_elements(By.CSS_SELECTOR, '.post-title')

    # Asercja że lista ma 20 elementów
    assert len(posts) == 20

    # Zamknięcie przeglądarki
    browser.quit()


def test_post_count_after_clicking_year_label():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    service = Service(ChromeDriverManager().install())
    browser = Chrome(service=service)
    browser.set_window_size(1920, 1080)

    # Otwarcie strony
    browser.get('http://www.awesome-testing.blogspot.com')
    years = browser.find_elements(By.CSS_SELECTOR, '#BlogArchive1_ArchiveList > ul')
    expected_number_of_posts = extract_the_number_of_posts_from_text(years[3].text)

    # Kliknięcie na labelkę
    browser.find_element(By.LINK_TEXT, '2019').click()

    # Pobranie listy tytułów
    posts = browser.find_elements(By.CSS_SELECTOR, '.post-title')

    # Asercja że lista ma odpowiednią ilość elementów (tj. tyle ile wyświetla się na UI)
    assert len(posts) == expected_number_of_posts

    # Zamknięcie przeglądarki
    browser.quit()


def extract_the_number_of_posts_from_text(text):
    match = re.search(r'\((\d+)\)', text)
    return int(match.group(1))
