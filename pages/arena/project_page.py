from selenium.webdriver.common.by import By


class ProjectPage:

    def __init__(self, browser):
        self.browser = browser

    def search_for_project(self, search_term):
        self.browser.find_element(By.CSS_SELECTOR, '#search').send_keys(search_term)
        self.browser.find_element(By.CSS_SELECTOR, '#j_searchButton').click()

    def verify_projects_found(self, search_term):
        found_projects = self.browser.find_elements(By.CSS_SELECTOR, 'tbody tr')
        assert len(found_projects) > 0

        names = self.browser.find_elements(By.CSS_SELECTOR, 'tbody tr td:nth-of-type(1)')
        for name in names:
            assert search_term in name.text.lower()

