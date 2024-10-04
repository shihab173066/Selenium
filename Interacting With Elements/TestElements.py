import time
from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.google.com/")

googleSearchBox = driver.find_element(By.ID, "APjFqb")
googleSearchBox.send_keys("Automation")
googleSearchBox.send_keys(Keys.RETURN)

time.sleep(3)
print("Done")