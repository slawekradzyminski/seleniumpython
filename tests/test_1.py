from selenium.webdriver import Chrome


def test_my_first_selenium_test():
    browser = Chrome()
    browser.get('http://demo.testarena.pl/zaloguj')
    assert browser.title.__contains__('TestArena')
    browser.quit()
