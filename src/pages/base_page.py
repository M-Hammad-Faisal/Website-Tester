import os
from src.config import Config
from src.config.framework import Element
from src.pages.selectors import Selectors


class BasePage:
    def __init__(self, element: Element, selectors: Selectors):
        self.element = element
        self.selectors = selectors
        self.screenshots_dir = Config.SCREENSHOTS_DIR
        os.makedirs(self.screenshots_dir, exist_ok=True)

    def screenshot(self, name: str):
        self.element.screenshot(f"{self.screenshots_dir}/{name}.png")
