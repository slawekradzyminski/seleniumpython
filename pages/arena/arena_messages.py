from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ArenaMessagesPage:

    def __init__(self, browser):
        self.browser = browser

    def wait_for_text_area_load(self):
        wait = WebDriverWait(self.browser, 10)
        text_area = (By.CSS_SELECTOR, '#j_msgContent')
        wait.until(expected_conditions.element_to_be_clickable(text_area))

    def insert_message(self, random_text):
        self.browser.find_element(By.CSS_SELECTOR, '#j_msgContent').send_keys(random_text)
