from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

def test_google_search():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("DevOps")
    search_box.submit()
    time.sleep(3)
    assert "DevOps" in driver.title
    driver.quit()
