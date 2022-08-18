from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest
import time


class BingSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def testSearchAutomation(self):
        self.driver.get("https://www.bing.com/")
        self.driver.find_element(By.ID, 'sb_form_q').send_keys("Arif")
        self.driver.find_element(By.ID, 'search_icon').click()

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.quit()
        print("Test Completed")

