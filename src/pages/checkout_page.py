from src.pages.base_page import BasePage


class CheckoutPage(BasePage):
    def fill_details(self, first_name: str, last_name: str, postal_code: str):
        self.element.fill(self.selectors.FIRST_NAME, first_name)
        self.element.fill(self.selectors.LAST_NAME, last_name)
        self.element.fill(self.selectors.POSTAL_CODE, postal_code)

    def continue_checkout(self):
        self.element.click(self.selectors.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.element.click(self.selectors.FINISH_BUTTON)

    def cancel(self):
        self.element.click(self.selectors.CANCEL_BUTTON)

    def is_loaded(self):
        return "checkout-step-one.html" in self.element.url() or "checkout-step-two.html" in self.element.url()

    def is_complete(self):
        return "checkout-complete.html" in self.element.url()

    def is_error_displayed(self):
        return self.element.is_visible(self.selectors.ERROR_MESSAGE)

    def get_total_price(self):
        return self.element.get_text(self.selectors.TOTAL_PRICE)

    def logout(self):
        self.element.click(self.selectors.MENU_BUTTON)
        self.element.click(self.selectors.LOGOUT_LINK)
