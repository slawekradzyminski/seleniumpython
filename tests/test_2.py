import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    # Initialize ChromeDriver
    driver = Chrome(executable_path=ChromeDriverManager().install())
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(3)

    # Return the driver object at the end of setup
    yield driver
    # For cleanup, quit the driver
    driver.quit()


def test_my_first_selenium_test(browser):
    browser.get('http://demo.testarena.pl/zaloguj')
    assert browser.title.__contains__('TestArena')


def test_login(browser):
    browser.get('http://demo.testarena.pl/zaloguj')
    email = browser.find_element(By.ID, 'email')
    password = browser.find_element(By.ID, 'password')
    login = browser.find_element(By.ID, 'login')

    email.send_keys('administrator@testarena.pl')
    password.send_keys('sumXQQ72$L')
    login.click()

    assert browser.title.__contains__('Cockpit')

