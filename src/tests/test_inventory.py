import allure


@allure.feature("Inventory")
class TestInventory:
    @allure.title("Add One Item to Cart")
    def test_add_one_item(self, pages, login_as_standard_user):
        inventory_page = pages["inventory"]
        inventory_page.add_first_item_to_cart()
        assert inventory_page.get_cart_count() == "1", "Item not added"

    @allure.title("Add Multiple Items to Cart")
    def test_add_multiple_items(self, pages, login_as_standard_user):
        inventory_page = pages["inventory"]
        inventory_page.add_first_item_to_cart()
        inventory_page.add_second_item_to_cart()
        assert inventory_page.get_cart_count() == "2", "Multiple items not added"

    @allure.title("Navigate to Item Details")
    def test_navigate_to_item(self, pages, login_as_standard_user):
        inventory_page = pages["inventory"]
        inventory_page.go_to_first_item()
        assert "inventory-item.html" in inventory_page.element.url(), "Navigation failed"

    @allure.title("Sort by Name A-Z")
    def test_sort_by_name_az(self, pages, login_as_standard_user):
        inventory_page = pages["inventory"]
        inventory_page.sort_by("az")
        items = inventory_page.get_item_names()
        assert items == sorted(items), "Items not sorted A-Z"

    @allure.title("Sort by Price Low-High")
    def test_sort_by_price_low_high(self, pages, login_as_standard_user):
        inventory_page = pages["inventory"]
        inventory_page.sort_by("lohi")
        prices = inventory_page.get_item_prices()
        assert prices == sorted(prices, key=float), "Prices not sorted low to high"
