import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture  # открытие браузера Chrome
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


