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
        
    def test_login(self):
        logger.info("Starting test: test_login")
        try:
            self.driver.get(self.base_url)
            logger.info("Successfully navigated to the account page")
            
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "login-btn"))
            )
            logger.debug("Login form found on page")
            
            self.driver.find_element(By.ID, "login-username").send_keys("admin")
            self.driver.find_element(By.ID, "login-password").send_keys("admin")
            self.driver.find_element(By.ID, "login-btn").click()
            logger.info("Login form submitted")
            
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "account-details"))
            )
            
            username = self.driver.find_element(By.ID, "username").text
            password = self.driver.find_element(By.ID, "password").text
            logger.info(f"Logged in as {username} with password {password}")
            
            self.assertEqual(username, "admin", "Username doesn't match expected value")
            self.assertEqual(password, "admin", "Password doesn't match expected value")
            logger.info("Successfully logged in")
            
        except Exception as e:
            logger.error(f"Failed to load login form: {str(e)}")
            raise
        
    def test_register(self):
        logger.info("Starting test: test_register")
        try:
            self.driver.get(self.base_url)
            logger.info("Successfully navigated to the account page")
            
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "login-switch"))
            ).click()
            
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "register-btn"))
            )
            
            self.driver.find_element(By.ID, "register-username").send_keys("testuser")
            self.driver.find_element(By.ID, "register-password").send_keys("testpassword")
            self.driver.find_element(By.ID, "register-email").send_keys("test@mail.com")
            self.driver.find_element(By.ID, "register-btn").click()
            logger.info("Register form submitted")
            
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "account-details"))
            )
            
            username = self.driver.find_element(By.ID, "username").text
            password = self.driver.find_element(By.ID, "password").text
            email = self.driver.find_element(By.ID, "email").text
            logger.info(f"Registered as {username} with password {password} and email {email}")
            
            self.assertEqual(username, "testuser", "Username doesn't match expected value")
            self.assertEqual(password, "testpassword", "Password doesn't match expected value")
            self.assertEqual(email, "test@mail.com", "Email doesn't match expected value")
            logger.info("Successfully registered")
            
        except Exception as e:
            logger.error(f"Failed to load login form: {str(e)}")
            raise
        
if __name__ == "__main__":
    unittest.main()