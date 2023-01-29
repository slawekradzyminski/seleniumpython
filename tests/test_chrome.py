import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

def test_example():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.bing.com/")
    driver.set_window_size(1280, 720)
    assert "Bing" in driver.title
    time.sleep(2)
    driver.quit()
