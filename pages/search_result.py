from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SearchResultPage:

    def __init__(self, browser):
        self.browser = browser

    # Oczekiwanie na załadowanie strony
    def wait_for_load(self):
        wait = WebDriverWait(self.browser, 10)
        grey_status_bar = (By.CLASS_NAME, 'status-msg-body')
        wait.until(expected_conditions.visibility_of_element_located(grey_status_bar))

    # weryfikacja liczby postów
    def verify_post_count(self, expected_count):
        titles = self.browser.find_elements(By.CLASS_NAME, 'post-title')
        assert len(titles) == expected_count
