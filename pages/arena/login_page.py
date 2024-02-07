from selenium.webdriver.common.by import By


class LoginPage:

    # Inicjalizacja klasy - przekazanie drivera/przeglądarki
    def __init__(self, browser):
        self.browser = browser

    # otwarcie
    def visit(self):
        self.browser.get('http://demo.testarena.pl/zaloguj')

    def login(self, email, password):
        self.browser.find_element(By.CSS_SELECTOR, '#email').send_keys(email)
        self.browser.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, '#login').click()
