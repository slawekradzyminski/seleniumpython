import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages.home import HomePage
from pages.search_result import SearchResultPage


@pytest.fixture()
def browser():
    driver = Chrome(executable_path=ChromeDriverManager().install())
    driver.get('https://awesome-testing.blogspot.com')
    yield driver
    driver.quit()


def test_post_count(browser):
    home_page = HomePage(browser)
    home_page.verify_post_count(4)


def test_post_count_after_search(browser):
    home_page = HomePage(browser)
    home_page.search_for('selenium')

    search_result_page = SearchResultPage(browser)
    search_result_page.wait_for_load()
    search_result_page.verify_post_count(20)


def test_post_count_on_2016_label(browser):
    home_page = HomePage(browser)
    home_page.click_label('2016')
    search_result_page = SearchResultPage(browser)
    search_result_page.verify_post_count(24)
