from selenium.webdriver.common.by import By


class ArenaHomePage:

    def __init__(self, browser):
        self.browser = browser

    def verify_displayed_email(self, email):
        user_info = self.browser.find_element(By.CSS_SELECTOR, '.user-info small')
        assert user_info.text == email

    def click_logout(self):
        self.browser.find_element(By.CSS_SELECTOR, '.icons-switch').click()

    def click_mail(self):
        self.browser.find_element(By.CSS_SELECTOR, '.icon_mail').click()

    def click_tools_icon(self):
        self.browser.find_element(By.CSS_SELECTOR, '.icon_tools').click()

