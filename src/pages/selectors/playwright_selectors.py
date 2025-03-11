class LoginSelectors:
    USERNAME_FIELD = "#user-name"
    PASSWORD_FIELD = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = ".error-message-container"


class InventorySelectors:
    FIRST_ITEM_ADD_BUTTON = ".inventory_item:nth-child(1) .btn_inventory"
    SECOND_ITEM_ADD_BUTTON = ".inventory_item:nth-child(2) .btn_inventory"
    FIRST_ITEM_LINK = ".inventory_item_name:first-child"
    CART_BADGE = ".shopping_cart_badge"
    SORT_DROPDOWN = ".product_sort_container"
    ITEM_NAMES = ".inventory_item_name"
    ITEM_PRICES = ".inventory_item_price"
    MENU_BUTTON = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"
    TWITTER_LINK = ".social_twitter a"
    FACEBOOK_LINK = ".social_facebook a"
    LINKEDIN_LINK = ".social_linkedin a"
    DETAILS_ADD_BUTTON = ".btn_inventory"
    DETAILS_REMOVE_BUTTON = ".btn_inventory.btn_secondary"
    DETAILS_ITEM_NAME = ".inventory_details_name"
    BACK_TO_INVENTORY = "#back-to-products"


class CartSelectors:
    CART_LINK = ".shopping_cart_link"
    CART_ITEMS = ".cart_item"
    REMOVE_FIRST_ITEM = ".cart_item:nth-child(3) .cart_button"
    CONTINUE_SHOPPING = "#continue-shopping"
    CHECKOUT_BUTTON = "#checkout"
    MENU_BUTTON = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"


class CheckoutSelectors:
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    FINISH_BUTTON = "#finish"
    CANCEL_BUTTON = "#cancel"
    ERROR_MESSAGE = ".error-message-container"
    TOTAL_PRICE = ".summary_total_label"
    MENU_BUTTON = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"
