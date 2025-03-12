from enum import StrEnum


class Page(StrEnum):
    LOGIN = "login"
    INVENTORY = "inventory"
    CART = "cart"
    CHECKOUT = "checkout"
