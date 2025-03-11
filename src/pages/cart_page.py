from src.pages.base_page import BasePage


class CartPage(BasePage):
    def navigate(self):
        self.element.click(self.selectors.CART_LINK)

    def get_item_count(self):
        items = self.element.get_all(self.selectors.CART_ITEMS)
        return len(items)

    def remove_first_item(self):
        try:
            self.element.click(self.selectors.REMOVE_FIRST_ITEM)
        except:
            pass

    def continue_shopping(self):
        self.element.click(self.selectors.CONTINUE_SHOPPING)

    def checkout(self):
        self.element.click(self.selectors.CHECKOUT_BUTTON)

    def is_loaded(self):
        return "cart.html" in self.element.url()

    def logout(self):
        self.element.click(self.selectors.MENU_BUTTON)
        self.element.click(self.selectors.LOGOUT_LINK)
