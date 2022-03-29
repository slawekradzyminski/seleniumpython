from selenium.webdriver.common.by import By


class ProfilePage:

    def __init__(self, browser):
        self.browser = browser

    def verify_email(self, login):
        assert self.browser.find_element(By.CLASS_NAME, 'content_label').text == login
