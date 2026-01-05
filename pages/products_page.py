from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    # Locators
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")

    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    REMOVE_BIKE_LIGHT = (By.ID, "remove-sauce-labs-bike-light")

    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def add_first_product(self):
        # click add + confirm it changed to Remove
        self.wait.until(EC.element_to_be_clickable(self.ADD_BACKPACK)).click()
        self.wait.until(EC.presence_of_element_located(self.REMOVE_BACKPACK))

    def add_second_product(self):
        # click add + confirm it changed to Remove
        self.wait.until(EC.element_to_be_clickable(self.ADD_BIKE_LIGHT)).click()
        self.wait.until(EC.presence_of_element_located(self.REMOVE_BIKE_LIGHT))

    def get_cart_count(self):
        # badge doesn't exist when cart is 0, so return 0 safely
        badges = self.driver.find_elements(*self.CART_BADGE)
        return int(badges[0].text) if badges else 0

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_LINK)).click()
