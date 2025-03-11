import pytest
import allure

@allure.feature("Item Details")
class TestItemDetails:
    @allure.title("Navigate to First Item Details")
    def test_navigate_to_first_item(self, pages, login_as_standard_user):
        inventory_page = pages["inventory"]
        inventory_page.go_to_first_item()
        assert "inventory-item.html" in inventory_page.element.url(), "Did not navigate to item details"

    @allure.title("Add Item to Cart from Details")
    def test_add_to_cart_from_details(self, pages, login_as_standard_user):
        inventory_page = pages["inventory"]
        inventory_page.go_to_first_item()
        inventory_page.add_item_from_details()
        assert inventory_page.get_cart_count() == "1", "Item not added from details"

    @allure.title("Remove Item from Details")
    def test_remove_from_details(self, pages, login_as_standard_user):
        inventory_page = pages["inventory"]
        inventory_page.go_to_first_item()
        inventory_page.add_item_from_details()
        inventory_page.remove_item_from_details()
        assert inventory_page.get_cart_count() == "0", "Item not removed from details"

    @allure.title("Verify Item Name in Details")
    def test_verify_item_name(self, pages, login_as_standard_user):
        inventory_page = pages["inventory"]
        inventory_page.go_to_first_item()
        name = inventory_page.get_item_name_from_details()
        assert name == "Sauce Labs Backpack", "Item name incorrect"  # First item on SauceDemo

    @allure.title("Back to Inventory from Details")
    def test_back_to_inventory(self, pages, login_as_standard_user):
        inventory_page = pages["inventory"]
        inventory_page.go_to_first_item()
        inventory_page.back_to_inventory()
        assert inventory_page.is_loaded(), "Did not return to inventory"