import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_testarena_login():
    administrator_email = 'administrator@testarena.pl'
    service = Service(ChromeDriverManager().install())
    browser = Chrome(service=service)
    browser.set_window_size(1920, 1080)
    browser.get('http://demo.testarena.pl/zaloguj')

    # Logowanie
    browser.find_element(By.CSS_SELECTOR, '#email').send_keys(administrator_email)
    browser.find_element(By.CSS_SELECTOR, '#password').send_keys('sumXQQ72$L')
    browser.find_element(By.CSS_SELECTOR, '#login').click()

    # Asercja
    user_email = browser.find_element(By.CSS_SELECTOR, '.user-info small').text
    assert user_email == administrator_email

    time.sleep(4)
    browser.quit()
