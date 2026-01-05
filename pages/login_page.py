from selenium.webdriver.common.by import By
import time


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_sauce_demo(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        username_field = self.driver.find_element(By.ID, "user-name")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username_field.clear()
        username_field.send_keys(username)
        password_field.clear()
        password_field.send_keys(password)
        login_button.click()

        time.sleep(5)
