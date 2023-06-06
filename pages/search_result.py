from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SearchResultPage:

    def __init__(self, browser):
        self.browser = browser

    def wait_for_load(self):
        wait = WebDriverWait(self.browser, 10)
        element_to_wait_for = (By.CSS_SELECTOR, '.status-msg-body')
        wait.until(expected_conditions.visibility_of_element_located(element_to_wait_for))

    def verify_post_count(self, expected_count):
        titles = self.browser.find_elements(By.CSS_SELECTOR, '.post-title')
        assert len(titles) == expected_count
