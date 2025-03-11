from src.config import Config
from src.pages.base_page import BasePage


class LoginPage(BasePage):
    def navigate(self):
        self.element.goto(Config.BASE_URL)

    def login(self, username: str, password: str):
        self.element.fill(self.selectors.USERNAME_FIELD, username)
        self.element.fill(self.selectors.PASSWORD_FIELD, password)
        self.element.click(self.selectors.LOGIN_BUTTON)

    def is_error_displayed(self):
        return self.element.is_visible(self.selectors.ERROR_MESSAGE)
