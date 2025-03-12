import allure

from src.config import Config


@allure.feature("Logout")
class TestLogout:
    @allure.title("Logout from Inventory Page")
    def test_logout_from_inventory(self, pages, login_as_standard_user):
        inventory_page, login_page = pages["inventory"], pages["login"]
        inventory_page.logout()
        assert login_page.element.url() == Config.BASE_URL, "Not redirected to login page"

    @allure.title("Logout from Cart Page")
    def test_logout_from_cart(self, pages, login_as_standard_user):
        inventory_page, cart_page, login_page = pages["inventory"], pages["cart"], pages["login"]
        inventory_page.add_first_item_to_cart()
        cart_page.navigate()
        cart_page.logout()
        assert login_page.element.url() == Config.BASE_URL, "Not redirected to login page"

    @allure.title("Logout from Checkout Step One")
    def test_logout_from_checkout_step_one(self, pages, login_as_standard_user):
        inventory_page, cart_page, checkout_page, login_page = (
            pages["inventory"],
            pages["cart"],
            pages["checkout"],
            pages["login"],
        )
        inventory_page.add_first_item_to_cart()
        cart_page.navigate()
        cart_page.checkout()
        checkout_page.logout()
        assert login_page.element.url() == Config.BASE_URL, "Not redirected to login page"

    @allure.title("Verify Menu Opens Before Logout")
    def test_menu_opens_before_logout(self, pages, login_as_standard_user):
        inventory_page = pages["inventory"]
        inventory_page.open_menu()
        assert inventory_page.is_menu_open(), "Menu not opened before logout"

    @allure.title("Logout Does Not Reset Cart")
    def test_logout_does_not_reset_cart(self, pages, login_as_standard_user):
        inventory_page, login_page = pages["inventory"], pages["login"]
        inventory_page.add_first_item_to_cart()
        assert inventory_page.get_cart_count() == "1", "Item not added"
        inventory_page.logout()
        login_page.login("standard_user", "secret_sauce")
        assert inventory_page.get_cart_count() == "1", "Cart should persist after logout"
