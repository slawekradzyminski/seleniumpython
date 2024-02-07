from selenium.webdriver.common.by import By


class HomePage:

    logout_icon = '.icons-switch'

    def __init__(self, browser):
        self.browser = browser

    def click_logout(self):
        self.browser.find_element(By.CSS_SELECTOR, self.logout_icon).click()

    def click_on_administrator_link(self):
        self.browser.find_element(By.CSS_SELECTOR, '.header_admin a').click()
