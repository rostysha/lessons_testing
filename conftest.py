from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


@pytest.fixture  # открытие браузера Chrome
def driver():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


