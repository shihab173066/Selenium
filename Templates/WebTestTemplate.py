# Importing the 'time' module to use its sleep function for adding delays in the script.
import time

# Importing the 'webdriver' from the 'selenium' module, which provides the main interface for controlling a web browser.
from selenium import webdriver

# Importing all necessary components from 'selenium.webdriver'.
from selenium.webdriver import *

# Importing 'Service' from 'selenium.webdriver.chrome.service' to manage the ChromeDriver service.
from selenium.webdriver.chrome.service import Service as ChromeService

# Importing 'By', a class that helps locate elements on a webpage by different methods (like ID, name, XPath, etc.).
from selenium.webdriver.common.by import By

# Importing 'ChromeDriverManager' from 'webdriver_manager.chrome' to automatically manage and install the ChromeDriver.
from webdriver_manager.chrome import ChromeDriverManager

""" ------------------------------------- Imports that are required -------------------------------------------------------------"""

# Initializing the Chrome WebDriver, setting up the service using the ChromeDriverManager, which installs the appropriate ChromeDriver.
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Opening the Google homepage using the get() method, which directs the browser to the specified URL.
driver.get("https://www.google.com/")

# Locating the Google search box element using its ID attribute ('APjFqb') and assigning it to the variable 'googleSearchBox'.
googleSearchBox = driver.find_element(By.ID, "APjFqb")

# Typing the word "Automation" into the search box using the send_keys() method.
googleSearchBox.send_keys("Automation")

# Simulating pressing the 'Enter' key to submit the search.
googleSearchBox.send_keys(Keys.RETURN)

# Pausing the execution for 3 seconds to allow the results page to load.
time.sleep(3)

# Printing "Done" in the console after the script completes the search and wait period.
print("Done")
