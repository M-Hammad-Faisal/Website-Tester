from src.config.framework.element import Element
from typing import List, Any


class PlaywrightElement(Element):
    def goto(self, url: str):
        self.context.goto(url)

    def click(self, locator: str):
        self.context.click(locator)

    def set_attribute(self, locator: str, attribute: str, value: str):
        function = f"(locator) => document.querySelector(locator).setAttribute('{attribute}','{value}')"
        self.context.evaluate(function, locator)

    def fill(self, locator: str, value: str):
        self.context.fill(locator, value)

    def select_option(self, locator: str, value: str):
        self.context.select_option(locator, value)

    def get_text(self, locator: str) -> str:
        return self.context.query_selector(locator).inner_text()

    def is_visible(self, locator: str) -> bool:
        return self.context.is_visible(locator)

    def get_all(self, locator: str) -> List[Any]:
        return self.context.query_selector_all(locator)

    def get_child(self, parent_locator: str, child_locator: str) -> "Element":
        parent = self.context.query_selector(parent_locator)
        child = parent.query_selector(child_locator)
        return PlaywrightElement(child)

    def get_all_texts(self, locator: str) -> List[str]:
        return [elem.inner_text() for elem in self.context.query_selector_all(locator)]

    def url(self) -> str:
        return self.context.url

    def screenshot(self, path: str):
        self.context.screenshot(path=path)
