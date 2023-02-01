import time

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def browser():
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.get('https://gemini.pl')
    yield browser
    browser.quit()


def test_waiting(browser):
    browser.execute_script("window.scrollTo(0, 600)")
    wait = WebDriverWait(browser, 10)
    grey_status_bar = (By.CSS_SELECTOR, "[name='Ramka produktowa 1 - Wysyłka 0 zł'] .swiper-slide-active")
    product = wait.until(EC.visibility_of_element_located(grey_status_bar))
    assert product.is_displayed()
