from selenium.webdriver.common.by import By


class ArenaProjectPage:

    def __init__(self, browser):
        self.browser = browser

    def verify_title(self, title):
        assert self.browser.find_element(By.CSS_SELECTOR, '.content_title').text == title
