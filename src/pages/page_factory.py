from enum import Enum
from typing import Any

from src.config.framework import Framework
from src.config.framework.element import ElementFactory

from src.pages.base_page import BasePage
from src.pages.page import Page
from .selectors import (
    SeleniumLoginSelectors,
    SeleniumInventorySelectors,
    SeleniumCartSelectors,
    SeleniumCheckoutSelectors,
    PlaywrightLoginSelectors,
    PlaywrightInventorySelectors,
    PlaywrightCartSelectors,
    PlaywrightCheckoutSelector,
)

from .login_page import LoginPage
from .inventory_page import InventoryPage
from .cart_page import CartPage
from .checkout_page import CheckoutPage

from src.pages import Pages


class PageFactory:
    @staticmethod
    def create_page(page_type: Page, context: Any, framework: Framework) -> Pages:
        element = ElementFactory.create_element(framework, context)

        if framework == Framework.PLAYWRIGHT:
            selectors_map: [str, Enum] = {
                Page.LOGIN: PlaywrightLoginSelectors,
                Page.INVENTORY: PlaywrightInventorySelectors,
                Page.CART: PlaywrightCartSelectors,
                Page.CHECKOUT: PlaywrightCheckoutSelector,
            }
        elif framework == Framework.SELENIUM:
            selectors_map: [str, Enum] = {
                Page.LOGIN: SeleniumLoginSelectors,
                Page.INVENTORY: SeleniumInventorySelectors,
                Page.CART: SeleniumCartSelectors,
                Page.CHECKOUT: SeleniumCheckoutSelectors,
            }
        else:
            raise ValueError(f"Unsupported framework: {framework}")

        page_map: [str, BasePage] = {
            Page.LOGIN: LoginPage,
            Page.INVENTORY: InventoryPage,
            Page.CART: CartPage,
            Page.CHECKOUT: CheckoutPage,
        }

        if page_type not in page_map:
            raise ValueError(f"Unknown page type: {page_type}")

        selectors = selectors_map[page_type]
        page_class = page_map[page_type]
        return page_class(element, selectors)
