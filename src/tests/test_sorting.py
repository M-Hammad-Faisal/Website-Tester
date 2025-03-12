import allure


@allure.feature("Sorting")
class TestSorting:
    @allure.title("Sort by Name Z-A")
    def test_sort_by_name_za(self, pages, login_as_standard_user):
        inventory_page = pages["inventory"]
        inventory_page.sort_by("za")
        items = inventory_page.get_item_names()
        assert items == sorted(items, reverse=True), "Items not sorted Z-A"

    @allure.title("Sort by Price High-Low")
    def test_sort_by_price_high_low(self, pages, login_as_standard_user):
        inventory_page = pages["inventory"]
        inventory_page.sort_by("hilo")
        prices = inventory_page.get_item_prices()
        assert prices == sorted(prices, key=float, reverse=True), "Prices not sorted high to low"

    @allure.title("Sort by Name A-Z After Z-A")
    def test_sort_name_az_after_za(self, pages, login_as_standard_user):
        inventory_page = pages["inventory"]
        inventory_page.sort_by("za")
        inventory_page.sort_by("az")
        items = inventory_page.get_item_names()
        assert items == sorted(items), "Items not sorted A-Z after Z-A"

    @allure.title("Sort by Price Low-High After High-Low")
    def test_sort_price_lohi_after_hilo(self, pages, login_as_standard_user):
        inventory_page = pages["inventory"]
        inventory_page.sort_by("hilo")
        inventory_page.sort_by("lohi")
        prices = inventory_page.get_item_prices()
        assert prices == sorted(prices, key=float), "Prices not sorted low to high after high-low"
