from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, browser):
        self.browser = browser

    def verify_post_count(self, expected_count):
        titles = self.browser.find_elements(By.CSS_SELECTOR, '.post-title')
        assert len(titles) == expected_count

    def search_for(self, query):
        search_bar = self.browser.find_element(By.CSS_SELECTOR, 'input.gsc-input')
        search_button = self.browser.find_element(By.CSS_SELECTOR, 'input.gsc-search-button')
        search_bar.send_keys(query)
        search_button.click()

    def click_label(self, label_text):
        label_element = self.browser.find_element(By.LINK_TEXT, label_text)
        label_element.click()
