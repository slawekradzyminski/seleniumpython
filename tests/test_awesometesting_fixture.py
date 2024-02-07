import re

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    # część która wykona się przed każdym testem
    service = Service(ChromeDriverManager().install())
    browser = Chrome(service=service)
    browser.set_window_size(1920, 1080)
    browser.get('http://www.awesome-testing.blogspot.com')

    # coś co przekazujemy do każdego testu
    yield browser

    # część która wykona się po każdym teście
    browser.quit()


def test_post_count(browser):
    posts = browser.find_elements(By.CSS_SELECTOR, '.post-title')
    assert len(posts) == 4


def test_post_count_after_search(browser):
    browser.find_element(By.CSS_SELECTOR, '.gsc-input input').send_keys('Selenium')
    browser.find_element(By.CSS_SELECTOR, '.gsc-search-button input').click()
    posts = browser.find_elements(By.CSS_SELECTOR, '.post-title')
    assert len(posts) == 20


def test_post_count_after_clicking_year_label(browser):
    years = browser.find_elements(By.CSS_SELECTOR, '#BlogArchive1_ArchiveList > ul')
    expected_number_of_posts = extract_the_number_of_posts_from_text(years[3].text)
    browser.find_element(By.LINK_TEXT, '2019').click()
    posts = browser.find_elements(By.CSS_SELECTOR, '.post-title')
    assert len(posts) == expected_number_of_posts


def extract_the_number_of_posts_from_text(text):
    match = re.search(r'\((\d+)\)', text)
    return int(match.group(1))
