from selenium.webdriver.common.by import By

class HomePage:

    # Pole dostępne dla wszystkich metod klasy
    URL = 'https://www.awesome-testing.com'
    post = (By.CLASS_NAME, 'post-title')

    # Inicjalizacja klasy - przekazanie drivera (przeglądarki)
    def __init__(self, browser):
        self.browser = browser

    # otwarcie strony
    def load(self):
        self.browser.get(self.URL)

    # weryfikacja liczby postów
    def verify_post_count(self, expectedCount):
        titles = self.browser.find_elements(*self.post)
        assert titles.__len__() == expectedCount

    # wyszukiwanie
    def search(self, search_term):
        searchbar = self.browser.find_element(By.CSS_SELECTOR, 'input.gsc-input')
        search_button = self.browser.find_element(By.CSS_SELECTOR, 'input.gsc-search-button')
        searchbar.send_keys(search_term)
        search_button.click()

    # klikanie na labelkę
    def click_label(self, param):
        cypress_label = self.browser.find_element(By.LINK_TEXT, 'Cypress')
        cypress_label.click()

