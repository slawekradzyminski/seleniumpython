from selenium.webdriver.common.by import By


class ArenaLoginPage:

    def __init__(self, browser):
        self.browser = browser

    def login(self, login, password):
        self.browser.find_element(By.ID, 'email').send_keys(login)
        self.browser.find_element(By.ID, 'password').send_keys(password)
        self.browser.find_element(By.ID, 'login').click()
