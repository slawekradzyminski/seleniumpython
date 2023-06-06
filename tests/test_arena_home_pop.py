import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from pages.arena.arena_home_page import ArenaHomePage
from pages.arena.arena_login import ArenaLoginPage
from pages.arena.arena_messages import ArenaMessagesPage
from pages.arena.arena_project_page import ArenaProjectPage


@pytest.fixture
def browser():
    driver = Chrome(executable_path=ChromeDriverManager().install())
    driver.get('http://demo.testarena.pl/zaloguj')
    arena_login_page = ArenaLoginPage(driver)
    arena_login_page.login('administrator@testarena.pl', 'sumXQQ72$L')
    yield driver
    driver.quit()


def test_should_display_email_in_user_section(browser):
    arena_home_page = ArenaHomePage(browser)
    arena_home_page.verify_displayed_email('administrator@testarena.pl')


def test_should_successfully_logout(browser):
    arena_home_page = ArenaHomePage(browser)
    arena_home_page.click_logout()
    assert browser.current_url == 'http://demo.testarena.pl/zaloguj'


def test_should_open_messages_and_display_text_area(browser):
    arena_home_page = ArenaHomePage(browser)
    arena_home_page.click_mail()
    arena_messages_page = ArenaMessagesPage(browser)
    arena_messages_page.wait_for_text_area_load()


def test_should_open_projects_page(browser):
    arena_home_page = ArenaHomePage(browser)
    arena_home_page.click_tools_icon()
    arena_project_page = ArenaProjectPage(browser)
    arena_project_page.verify_title('Projekty')

