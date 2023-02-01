from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PanelPage:
    def __init__(self, browser):
        self.browser = browser

    def wait_for_load(self):
        wait = WebDriverWait(self.browser, 10)
        selector = (By.CSS_SELECTOR, '.j_msgResponse')
        return wait.until(expected_conditions.element_to_be_clickable(selector))
