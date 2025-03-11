from src.pages.base_page import BasePage

class InventoryPage(BasePage):
    def add_first_item_to_cart(self):
        self.element.click(self.selectors.FIRST_ITEM_ADD_BUTTON)

    def add_second_item_to_cart(self):
        self.element.click(self.selectors.SECOND_ITEM_ADD_BUTTON)

    def go_to_first_item(self):
        self.element.click(self.selectors.FIRST_ITEM_LINK)

    def get_cart_count(self):
        try:
            return self.element.get_text(self.selectors.CART_BADGE)
        except:
            return "0"

    def is_loaded(self):
        return "inventory.html" in self.element.url()

    def sort_by(self, option):
        self.element.select_option(self.selectors.SORT_DROPDOWN, option)

    def get_item_names(self):
        return self.element.get_all_texts(self.selectors.ITEM_NAMES)

    def get_item_prices(self):
        return [price.replace("$", "") for price in self.element.get_all_texts(self.selectors.ITEM_PRICES)]

    def open_menu(self):
        self.element.click(self.selectors.MENU_BUTTON)

    def is_menu_open(self):
        return self.element.is_visible(self.selectors.LOGOUT_LINK)

    def logout(self):
        self.open_menu()
        self.element.click(self.selectors.LOGOUT_LINK)

    def __set_target_self(self, selector: str):
        self.element.set_attribute(selector, "target", "_self")

    def click_twitter_link(self):
        self.__set_target_self(self.selectors.TWITTER_LINK)
        self.element.click(self.selectors.TWITTER_LINK)

    def click_facebook_link(self):
        self.__set_target_self(self.selectors.FACEBOOK_LINK)
        self.element.click(self.selectors.FACEBOOK_LINK)

    def click_linkedin_link(self):
        self.__set_target_self(self.selectors.LINKEDIN_LINK)
        self.element.click(self.selectors.LINKEDIN_LINK)

    def add_item_from_details(self):
        self.element.click(self.selectors.DETAILS_ADD_BUTTON)

    def remove_item_from_details(self):
        self.element.click(self.selectors.DETAILS_REMOVE_BUTTON)

    def get_item_name_from_details(self):
        return self.element.get_text(self.selectors.DETAILS_ITEM_NAME)

    def back_to_inventory(self):
        self.element.click(self.selectors.BACK_TO_INVENTORY)

