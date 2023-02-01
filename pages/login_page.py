from selenium.webdriver.common.by import By


class LoginPage:
    # zmienne dostępne dla wszystkich metod w danej klasie
    URL = 'http://demo.testarena.pl/zaloguj'

    # konstruktor (metoda służąca do tworzenia obiektu tej klasy)
    def __init__(self, browser):
        self.browser = browser

    # metody danej klasy (akcje które można wywołać na stronie)
    def load(self):
        self.browser.get(self.URL)

    def login(self, login, password):
        self.browser.find_element(By.CSS_SELECTOR, "#email").send_keys(login)
        self.browser.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, "#login").click()

