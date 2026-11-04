from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

from selenium.webdriver.remote.webelement import WebElement


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
# driver он же браузер


# Это тест открытия ссылки на самунг с6
def test_open_s6(driver):
    driver.get('https://www.demoblaze.com/index.html')
    galaxy_s6 = driver.find_element(By.LINK_TEXT, value="Samsung galaxy s6")
    galaxy_s6.click()
    title = driver.find_element(By.CSS_SELECTOR, value="h2")
    assert title.text == "Samsung galaxy s6"


def test_two_monitors(driver):
    driver.get('https://www.demoblaze.com/index.html')
    monitors_link = driver.find_element(By.CSS_SELECTOR, 'a[onclick*="monitor"]')
    time.sleep(10)
    monitors_link.click()
    time.sleep(2)
    monitors = driver.find_elements(By.CSS_SELECTOR,value=".card")
    assert len(monitors) == 2