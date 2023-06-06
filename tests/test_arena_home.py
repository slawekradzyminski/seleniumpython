import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    driver = Chrome(executable_path=ChromeDriverManager().install())
    driver.get('http://demo.testarena.pl/zaloguj')
    driver.find_element(By.ID, 'email').send_keys('administrator@testarena.pl')
    driver.find_element(By.ID, 'password').send_keys('sumXQQ72$L')
    driver.find_element(By.ID, 'login').click()
    yield driver
    driver.quit()


def test_should_display_email_in_user_section(browser):
    user_info = browser.find_element(By.CSS_SELECTOR, '.user-info small')
    assert user_info.text == 'administrator@testarena.pl'


def test_should_successfully_logout(browser):
    browser.find_element(By.CSS_SELECTOR, '.icons-switch').click()
    assert browser.current_url == 'http://demo.testarena.pl/zaloguj'


def test_should_open_messages_and_display_text_area(browser):
    browser.find_element(By.CSS_SELECTOR, '.icon_mail').click()
    wait = WebDriverWait(browser, 10)
    text_area = (By.CSS_SELECTOR, '#j_msgContent')
    wait.until(expected_conditions.element_to_be_clickable(text_area))


def test_should_open_projects_page(browser):
    browser.find_element(By.CSS_SELECTOR, '.icon_tools').click()
    assert browser.find_element(By.CSS_SELECTOR, '.content_title').text == 'Projekty'
