import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_google_search():
    # Initialize WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    
    # Open Google
    driver.get("https://google.com")
    
    # Locate the search box using the 'name' attribute and perform a search
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)
    
    time.sleep(2)
    print("Test Completed")
    
    # Close the browser
    driver.quit()