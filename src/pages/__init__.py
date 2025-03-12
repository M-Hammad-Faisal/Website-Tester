from .inventory_page import InventoryPage
from .login_page import LoginPage

type Pages = type[LoginPage or InventoryPage]
