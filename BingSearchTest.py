from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.bing.com/")
driver.find_element(By.ID, 'sb_form_q').send_keys("Arif")
driver.find_element(By.ID, 'search_icon').click()

time.sleep(10)
driver.quit()
print("Test Completed")


