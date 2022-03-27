from selenium.webdriver import Chrome
from selenium.webdriver import Edge
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time


def test_should_close_consent():
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.get('https://www.google.pl')
    assert browser.find_element(By.CSS_SELECTOR, "[title='Before you continue to Google Search']").get_attribute(
        "style") == 'display: block;'
    browser.find_element(By.XPATH, "//div[text()='I agree']").click()
    assert browser.find_element(By.CSS_SELECTOR, "[title='Before you continue to Google Search']").get_attribute(
        "style") == 'display: none;'


def test_hide_google_consent():
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.get('https://www.google.pl')
    browser.delete_cookie('CONSENT')
    browser.add_cookie({'name': 'CONSENT', 'value': 'YES+shp.gws-20220322-0-RC3.en+FX+361'})
    browser.refresh()


def test_should_close_consent():
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.get('https://www.google.pl')
    agree = browser.find_element(By.XPATH, '//*[@id="L2AGLb"]/div')
    agree.click()
    assert agree.is_displayed() is False
    time.sleep(3)
