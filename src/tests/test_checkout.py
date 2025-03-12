import allure


@allure.feature("Checkout")
class TestCheckout:
    @allure.title("Complete Checkout with Valid Details")
    def test_checkout_valid(self, pages, login_as_standard_user):
        inventory_page, cart_page, checkout_page = pages["inventory"], pages["cart"], pages["checkout"]
        inventory_page.add_first_item_to_cart()
        cart_page.navigate()
        cart_page.checkout()
        checkout_page.fill_details("John", "Doe", "12345")
        checkout_page.continue_checkout()
        checkout_page.finish_checkout()
        assert checkout_page.is_complete(), "Checkout not completed"

    @allure.title("Checkout with Missing First Name")
    def test_checkout_missing_first_name(self, pages, login_as_standard_user):
        inventory_page, cart_page, checkout_page = pages["inventory"], pages["cart"], pages["checkout"]
        inventory_page.add_first_item_to_cart()
        cart_page.navigate()
        cart_page.checkout()
        checkout_page.fill_details("", "Doe", "12345")
        checkout_page.continue_checkout()
        assert checkout_page.is_error_displayed(), "Error not shown for missing first name"

    @allure.title("Checkout with Missing Postal Code")
    def test_checkout_missing_postal_code(self, pages, login_as_standard_user):
        inventory_page, cart_page, checkout_page = pages["inventory"], pages["cart"], pages["checkout"]
        inventory_page.add_first_item_to_cart()
        cart_page.navigate()
        cart_page.checkout()
        checkout_page.fill_details("John", "Doe", "")
        checkout_page.continue_checkout()
        assert checkout_page.is_error_displayed(), "Error not shown for missing postal code"

    @allure.title("Cancel Checkout and Return to Cart")
    def test_cancel_checkout(self, pages, login_as_standard_user):
        inventory_page, cart_page, checkout_page = pages["inventory"], pages["cart"], pages["checkout"]
        inventory_page.add_first_item_to_cart()
        cart_page.navigate()
        cart_page.checkout()
        checkout_page.cancel()
        assert cart_page.is_loaded(), "Did not return to cart page"

    @allure.title("Verify Total Price in Checkout")
    def test_verify_total_price(self, pages, login_as_standard_user):
        inventory_page, cart_page, checkout_page = pages["inventory"], pages["cart"], pages["checkout"]
        inventory_page.add_first_item_to_cart()
        cart_page.navigate()
        cart_page.checkout()
        checkout_page.fill_details("John", "Doe", "12345")
        checkout_page.continue_checkout()
        total = checkout_page.get_total_price()
        assert total.startswith("Total: $"), "Total price not displayed correctly"
