from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def test_my_first_firefox_selenium_test():
    browser = Firefox(executable_path=GeckoDriverManager().install())
    browser.get('http://demo.testarena.pl/zaloguj')
    assert browser.title.__contains__('TestArena')
    browser.quit()


def test_my_first_chrome_selenium_test():
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.get('http://demo.testarena.pl/zaloguj')
    assert browser.title.__contains__('TestArena')
    browser.quit()
