import allure
import time


@allure.feature("Performance")
class TestPerformance:
    @allure.title("Measure Login Page Load Time")
    def test_login_page_load_time(self, pages):
        login_page = pages["login"]
        start_time = time.time()
        login_page.navigate()
        load_time = time.time() - start_time
        assert load_time < 6, f"Login page load time {load_time:.2f}s exceeded 5s"

    @allure.title("Measure Inventory Page Load Time After Login")
    def test_inventory_page_load_time(self, pages):
        login_page = pages["login"]
        login_page.navigate()
        start_time = time.time()
        login_page.login("standard_user", "secret_sauce")
        load_time = time.time() - start_time
        assert load_time < 6, f"Inventory page load time {load_time:.2f}s exceeded 5s"

    @allure.title("Measure Add to Cart Response Time")
    def test_add_to_cart_response_time(self, pages, login_as_standard_user):
        inventory_page = pages["inventory"]
        start_time = time.time()
        inventory_page.add_first_item_to_cart()
        response_time = time.time() - start_time
        assert response_time < 2, f"Add to cart response time {response_time:.2f}s exceeded 2s"

    @allure.title("Measure Cart Page Load Time")
    def test_cart_page_load_time(self, pages, login_as_standard_user):
        inventory_page, cart_page = pages["inventory"], pages["cart"]
        inventory_page.add_first_item_to_cart()
        start_time = time.time()
        cart_page.navigate()
        load_time = time.time() - start_time
        assert load_time < 3, f"Cart page load time {load_time:.2f}s exceeded 3s"

    @allure.title("Measure Checkout Step One Load Time")
    def test_checkout_step_one_load_time(self, pages, login_as_standard_user):
        inventory_page, cart_page = pages["inventory"], pages["cart"]
        inventory_page.add_first_item_to_cart()
        cart_page.navigate()
        start_time = time.time()
        cart_page.checkout()
        load_time = time.time() - start_time
        assert load_time < 3, f"Checkout step one load time {load_time:.2f}s exceeded 3s"

    @allure.title("Measure Checkout Completion Time")
    def test_checkout_completion_time(self, pages, login_as_standard_user):
        inventory_page, cart_page, checkout_page = pages["inventory"], pages["cart"], pages["checkout"]
        inventory_page.add_first_item_to_cart()
        cart_page.navigate()
        cart_page.checkout()
        checkout_page.fill_details("John", "Doe", "12345")
        start_time = time.time()
        checkout_page.continue_checkout()
        checkout_page.finish_checkout()
        completion_time = time.time() - start_time
        assert completion_time < 6, f"Checkout completion time {completion_time:.2f}s exceeded 5s"

    @allure.title("Measure Logout Response Time")
    def test_logout_response_time(self, pages, login_as_standard_user):
        inventory_page = pages["inventory"]
        start_time = time.time()
        inventory_page.logout()
        response_time = time.time() - start_time
        assert response_time < 2, f"Logout response time {response_time:.2f}s exceeded 2s"
