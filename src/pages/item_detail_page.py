from src.pages.base_page import BasePage


class ItemDetailsPage(BasePage):
    def add_to_cart(self):
        self.element.click(self.selectors.ADD_TO_CART_BUTTON)

    def get_item_name(self):
        return self.element.get_text(self.selectors.ITEM_NAME)

    def get_item_price(self):
        return self.element.get_text(self.selectors.ITEM_PRICE)

    def back_to_inventory(self):
        self.element.click(self.selectors.BACK_BUTTON)

    def is_loaded(self):
        return "inventory-item.html" in self.element.url()
