import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def drivers():
    chrome_driver = webdriver.Chrome()
    firefox_driver = webdriver.Firefox()
    yield chrome_driver, firefox_driver
    chrome_driver.quit()
    firefox_driver.quit()

