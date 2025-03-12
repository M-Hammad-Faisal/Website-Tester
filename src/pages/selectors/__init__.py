from .selenium_selectors import (
    LoginSelectors as SeleniumLoginSelectors,
    InventorySelectors as SeleniumInventorySelectors,
    CheckoutSelectors as SeleniumCheckoutSelectors,
    CartSelectors as SeleniumCartSelectors,
)
from .playwright_selectors import (
    LoginSelectors as PlaywrightLoginSelectors,
    InventorySelectors as PlaywrightInventorySelectors,
    CheckoutSelectors as PlaywrightCheckoutSelector,
    CartSelectors as PlaywrightCartSelectors,
)

type Selectors = type[
    SeleniumLoginSelectors
    or SeleniumInventorySelectors
    or SeleniumCartSelectors
    or SeleniumCheckoutSelectors
    or PlaywrightLoginSelectors
    or PlaywrightInventorySelectors
    or PlaywrightCartSelectors
    or PlaywrightCheckoutSelector
]

__all__ = [
    "Selectors",
    "SeleniumLoginSelectors",
    "SeleniumInventorySelectors",
    "SeleniumCheckoutSelectors",
    "SeleniumCartSelectors",
    "PlaywrightLoginSelectors",
    "PlaywrightInventorySelectors",
    "PlaywrightCheckoutSelector",
    "PlaywrightCartSelectors",
]
