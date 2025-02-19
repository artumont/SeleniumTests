import unittest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class EcommerceTests(unittest.TestCase):
    def setUp(self):
        logger.info("Setting up test environment")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "http://127.0.0.1:5000/ecommerce_test"
        logger.info(f"Test environment setup completed. Base URL: {self.base_url}")
        
    def tearDown(self):
        logger.info("Tearing down test environment")
        self.driver.quit()
        logger.info("Browser session ended")
        
    def test_add_items_to_cart(self):
        logger.info("Starting test: add_items_to_cart")
        try:
            self.driver.get(self.base_url)
            logger.info("Successfully navigated to the e-commerce page")
            
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "product"))
            )
            logger.debug("Product elements found on page")
            
            items = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'add-to-cart-btn'))
            )
            item_count = len(items)
            logger.info(f"Found {item_count} products available for purchase")
            
            for idx, item in enumerate(items, 1):
                logger.debug(f"Attempting to add item {idx}/{item_count} to cart")
                item.click()
                try:
                    cart_items = self.driver.execute_script("return (cart || []).length;")
                    logger.info(f"Successfully added item {idx}. Cart now contains {cart_items} items")
                except Exception as e:
                    logger.error(f"Failed to verify cart contents after adding item {idx}: {str(e)}")
                    raise
                    
            cart_count = self.driver.execute_script("return (cart || []).length;")
            logger.info(f"Final cart count: {cart_count}")
            self.assertEqual(item_count, cart_count, f"Cart count ({cart_count}) doesn't match number of added items ({item_count})")
            logger.info("Test add_items_to_cart completed successfully")
            
        except Exception as e:
            logger.error(f"Test add_items_to_cart failed: {str(e)}", exc_info=True)
            raise
            
    def test_perform_checkout(self):
        logger.info("Starting test: perform_checkout")
        try:
            self.driver.get(self.base_url)
            logger.info("Successfully navigated to the e-commerce page")
            
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "product"))
            )
            logger.debug("Product elements found on page")
            
            items = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'add-to-cart-btn'))
            )
            item_count = len(items)
            logger.info(f"Found {item_count} items")
            
            for item in items:
                item.click()
                try:
                    cart_items = self.driver.execute_script("return (cart || []).length;")
                    logger.info(f"Current cart size: {cart_items}")
                except Exception as e:
                    logger.error(f"Failed to read cart: {str(e)}")
                    raise
                    
            cart_count = self.driver.execute_script("return (cart || []).length;")
            self.assertEqual(item_count, cart_count, "Cart count doesn't match number of added items")
            logger.info("All items are added to cart")
            
            logger.info("Beginning checkout process")
            cart_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "view-cart-btn"))
            )
            cart_button.click()
            logger.debug("Cart view opened")
            
            checkout_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "checkout-btn"))
            )
            checkout_button.click()
            logger.debug("Checkout process initiated")
            
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'checkout-form'))
            )
            
            logger.info("Filling out checkout form")
            test_data = {
                'name': "John Doe",
                'email': "johndoe@testmail.com",
                'address': "123 Main St",
                'card-number': "5558016839301661",
                'expiry-date': "12/23",
                'cvv': "123"
            }
            
            for field, value in test_data.items():
                element = self.driver.find_element(By.ID, field)
                element.send_keys(value)
                logger.debug(f"Filled {field} field with test data")
                actual_value = element.get_attribute("value")
                self.assertEqual(actual_value, value, f"Field {field} value mismatch")
                logger.debug(f"Verified {field} field value")
            
            logger.info("Submitting order")
            place_order_button = self.driver.find_element(By.ID, 'place-order-btn')
            place_order_button.click()
            
            logger.info("Waiting for order confirmation")
            confirmation_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'order-confirmation'))
            )
            
            order_confirmation_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="order-confirmation"]/h2'))
            )
            self.assertEqual(order_confirmation_text.text, "Order Confirmed!", "Order confirmation text doesn't match")
            
            order_number = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'order-number'))
            ).text
            logger.info(f"Order successfully placed. Order number: {order_number}")
            
            self.assertTrue(order_number.startswith("ORDER-"), "Invalid order number format")
            logger.info("Test perform_checkout completed successfully")
        
        except Exception as e:
            logger.error(f"Test perform_checkout failed: {str(e)}", exc_info=True)
            raise
        
if __name__ == "__main__":
    logger.info("Starting E-commerce test suite")
    unittest.main()