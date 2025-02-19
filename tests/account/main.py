import unittest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class AccountTests(unittest.TestCase):
    def setUp(self):
        logger.info("Setting up test environment")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "http://127.0.0.1:5000/account_test"
        logger.info(f"Test environment setup completed. Base URL: {self.base_url}")
        
    def tearDown(self):
        logger.info("Tearing down test environment")
        self.driver.quit()
        logger.info("Browser session ended")