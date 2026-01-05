from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_first_product(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    def add_second_product(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

    def get_cart_count(self):
        badge = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        return int(badge.text)

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
