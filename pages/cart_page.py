from selenium.webdriver.common.by import By
import time

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def remove_one_product(self):
        self.driver.find_element(By.CLASS_NAME, "cart_button").click()
    time.sleep(2)

    def get_cart_count(self):
        return int(
            self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        )
    time.sleep(2)
