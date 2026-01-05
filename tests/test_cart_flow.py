import time
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_add_and_remove_product(browser):

    # Login
    login_page = LoginPage(browser)
    login_page.open_sauce_demo()
    login_page.login("standard_user", "secret_sauce")
    time.sleep(2)

    # Add two products
    products_page = ProductsPage(browser)
    products_page.add_first_product()
    time.sleep(2)
    products_page.add_second_product()
    time.sleep(2)

    # Verify cart count is 2
    assert products_page.get_cart_count() == 2
    time.sleep(2)

    # Go to cart
    products_page.go_to_cart()
    time.sleep(2)

    # Remove one product
    cart_page = CartPage(browser)
    cart_page.remove_one_product()
    time.sleep(2)

    # Verify cart count is 1
    assert cart_page.get_cart_count() == 1
    time.sleep(2)

    print("Test completed successfully.")
    
