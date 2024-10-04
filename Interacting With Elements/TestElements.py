import time
from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://trytestingthis.netlify.app/index.html/")
driver.find_element(By.ID, "fname").send_keys("Mr")
driver.find_element(By.ID, "lname").send_keys("Who")
time.sleep(5)
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
time.sleep(8)
print("Done")