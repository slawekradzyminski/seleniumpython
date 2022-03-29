from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:

    def __init__(self, browser):
        self.browser = browser

    def wait_for_load(self):
        wait = WebDriverWait(self.browser, 10)
        grey_bar = (By.LINK_TEXT, 'Kokpit')
        wait.until(expected_conditions.presence_of_element_located(grey_bar))

    def logout(self):
        self.browser.find_element(By.CLASS_NAME, 'header_logout').click()

    def go_to_user_profile(self):
        self.browser.find_element(By.CLASS_NAME, 'user-info').click()
