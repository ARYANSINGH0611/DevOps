from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the driver (make sure you have the ChromeDriver installed)
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Find the search box
search_box = driver.find_element(By.NAME, "q")

# Type something and press Enter
search_box.send_keys("Selenium Python example")
search_box.send_keys(Keys.RETURN)

# Wait for a few seconds to see results
time.sleep(3)

# Close the browser
driver.quit()
