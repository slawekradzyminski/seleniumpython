from selenium.webdriver.common.by import By


class CockpitPage:
    def __init__(self, browser):
        self.browser = browser

    def click_envelope(self):
        envelope = self.browser.find_element(By.CSS_SELECTOR, '.top_messages')
        envelope.click()

    def click_administration(self):
        admin_button = self.browser.find_element(By.CSS_SELECTOR, '[title=Administracja]')
        admin_button.click()


