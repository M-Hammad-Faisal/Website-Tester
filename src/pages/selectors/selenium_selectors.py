from selenium.webdriver.common.by import By


class LoginSelectors:
    URL = "https://www.saucedemo.com/"
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message-container")


class InventorySelectors:
    FIRST_ITEM_ADD_BUTTON = (By.CSS_SELECTOR, ".inventory_item:nth-child(1) .btn_inventory")
    SECOND_ITEM_ADD_BUTTON = (By.CSS_SELECTOR, ".inventory_item:nth-child(2) .btn_inventory")
    FIRST_ITEM_LINK = (By.CSS_SELECTOR, ".inventory_item_name:first-child")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    SORT_DROPDOWN = (By.CSS_SELECTOR, ".product_sort_container")
    ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    ITEM_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    TWITTER_LINK = (By.CSS_SELECTOR, ".social_twitter a")
    FACEBOOK_LINK = (By.CSS_SELECTOR, ".social_facebook a")
    LINKEDIN_LINK = (By.CSS_SELECTOR, ".social_linkedin a")
    DETAILS_ADD_BUTTON = (By.CSS_SELECTOR, ".btn_inventory")
    DETAILS_REMOVE_BUTTON = (By.CSS_SELECTOR, ".btn_inventory.btn_secondary")
    DETAILS_ITEM_NAME = (By.CSS_SELECTOR, ".inventory_details_name")
    BACK_TO_INVENTORY = (By.ID, "back-to-products")


class CartSelectors:
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    REMOVE_FIRST_ITEM = (By.CSS_SELECTOR, ".cart_item:nth-child(3) .cart_button")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")


class CheckoutSelectors:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message-container")
    TOTAL_PRICE = (By.CSS_SELECTOR, ".summary_total_label")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
