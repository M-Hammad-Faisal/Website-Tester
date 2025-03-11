import pytest
import allure

@allure.feature("Cart")
class TestCart:
    @allure.title("View Cart After Adding One Item")
    def test_view_cart_one_item(self, pages, login_as_standard_user):
        inventory_page, cart_page = pages["inventory"], pages["cart"]
        inventory_page.add_first_item_to_cart()
        cart_page.navigate()
        assert cart_page.get_item_count() == 1, "Cart should have 1 item"

    @allure.title("View Cart After Adding Multiple Items")
    def test_view_cart_multiple_items(self, pages, login_as_standard_user):
        inventory_page, cart_page = pages["inventory"], pages["cart"]
        inventory_page.add_first_item_to_cart()
        inventory_page.add_second_item_to_cart()
        cart_page.navigate()
        assert cart_page.get_item_count() == 2, "Cart should have 2 items"

    @allure.title("Remove Item from Cart")
    def test_remove_item(self, pages, login_as_standard_user):
        inventory_page, cart_page = pages["inventory"], pages["cart"]
        inventory_page.add_first_item_to_cart()
        cart_page.navigate()
        cart_page.remove_first_item()
        assert cart_page.get_item_count() == 0, "Item not removed from cart"

    @allure.title("Continue Shopping from Cart")
    def test_continue_shopping(self, pages, login_as_standard_user):
        inventory_page, cart_page = pages["inventory"], pages["cart"]
        inventory_page.add_first_item_to_cart()
        cart_page.navigate()
        cart_page.continue_shopping()
        assert inventory_page.is_loaded(), "Did not return to inventory page"

    @allure.title("Proceed to Checkout from Cart")
    def test_proceed_to_checkout(self, pages, login_as_standard_user):
        inventory_page, cart_page, checkout_page = pages["inventory"], pages["cart"], pages["checkout"]
        inventory_page.add_first_item_to_cart()
        cart_page.navigate()
        cart_page.checkout()
        assert checkout_page.is_loaded(), "Did not navigate to checkout page"