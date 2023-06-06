import time

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions

from utils.random_message import generate_random_text


@pytest.fixture()
def browser():
    driver = Chrome(executable_path=ChromeDriverManager().install())
    driver.get('http://demo.testarena.pl/zaloguj')
    driver.find_element(By.ID, 'email').send_keys('administrator@testarena.pl')
    driver.find_element(By.ID, 'password').send_keys('sumXQQ72$L')
    driver.find_element(By.ID, 'login').click()
    driver.find_element(By.CSS_SELECTOR, '.icon_mail').click()
    wait = WebDriverWait(driver, 10)
    text_area = (By.CSS_SELECTOR, '#j_msgContent')
    wait.until(expected_conditions.element_to_be_clickable(text_area))
    yield driver
    driver.quit()


def test_should_add_new_message(browser):
    random_text = generate_random_text(10)


