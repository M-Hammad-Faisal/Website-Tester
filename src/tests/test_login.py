import allure

from src.pages.page import Page


@allure.feature("Login")
class TestLogin:
    @allure.title("Login with Valid Credentials")
    def test_login_valid(self, pages):
        login_page, inventory_page = pages[Page.LOGIN], pages[Page.INVENTORY]
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        assert inventory_page.is_loaded(), "Login failed"

    @allure.title("Login with Problem User")
    def test_login_problem_user(self, pages):
        login_page, inventory_page = pages[Page.LOGIN], pages[Page.INVENTORY]
        login_page.navigate()
        login_page.login("problem_user", "secret_sauce")
        assert inventory_page.is_loaded(), "Problem user login failed"

    @allure.title("Login with Invalid Username")
    def test_login_invalid_username(self, pages):
        login_page = pages[Page.LOGIN]
        login_page.navigate()
        login_page.login("invalid_user", "secret_sauce")
        assert login_page.is_error_displayed(), "Error not shown for invalid username"

    @allure.title("Login with Invalid Password")
    def test_login_invalid_password(self, pages):
        login_page = pages[Page.LOGIN]
        login_page.navigate()
        login_page.login("standard_user", "wrong_pass")
        assert login_page.is_error_displayed(), "Error not shown for invalid password"

    @allure.title("Login with Locked User")
    def test_login_locked_user(self, pages):
        login_page = pages[Page.LOGIN]
        login_page.navigate()
        login_page.login("locked_out_user", "secret_sauce")
        assert login_page.is_error_displayed(), "Locked user should fail"

    @allure.title("Login with Empty Credentials")
    def test_login_empty_credentials(self, pages):
        login_page = pages[Page.LOGIN]
        login_page.navigate()
        login_page.login("", "")
        assert login_page.is_error_displayed(), "Empty creds should fail"
