import pytest
import allure

@allure.feature("Error Handling")
class TestErrorHandling:
    @allure.title("Login with Performance Glitch User")
    def test_performance_glitch_user(self, pages):
        login_page, inventory_page = pages["login"], pages["inventory"]
        login_page.navigate()
        login_page.login("performance_glitch_user", "secret_sauce")
        assert inventory_page.is_loaded(), "Performance glitch user login failed"

    @allure.title("Add Max Items to Cart")
    def test_add_max_items(self, pages, login_as_standard_user):
        inventory_page = pages["inventory"]
        inventory_page.add_first_item_to_cart()
        inventory_page.add_second_item_to_cart()
        assert inventory_page.get_cart_count() in ["2", "6"], "Did not add items to cart"

    @allure.title("Checkout with Invalid Postal Code")
    def test_checkout_invalid_postal_code(self, pages, login_as_standard_user):
        inventory_page, cart_page, checkout_page = pages["inventory"], pages["cart"], pages["checkout"]
        inventory_page.add_first_item_to_cart()
        cart_page.navigate()
        cart_page.checkout()
        checkout_page.fill_details("John", "Doe", "abcde")
        checkout_page.continue_checkout()
        assert not checkout_page.is_error_displayed(), "SauceDemo accepts invalid postal codes"

    @allure.title("Remove Non-Existent Item from Cart")
    def test_remove_empty_cart(self, pages, login_as_standard_user):
        cart_page = pages["cart"]
        cart_page.navigate()
        cart_page.remove_first_item()
        assert cart_page.get_item_count() == 0, "Cart should remain empty"

    @allure.title("Checkout with Empty Cart")
    def test_checkout_empty_cart(self, pages, login_as_standard_user):
        cart_page, checkout_page = pages["cart"], pages["checkout"]
        cart_page.navigate()
        cart_page.checkout()
        assert checkout_page.is_loaded(), "SauceDemo allows checkout with empty cart"