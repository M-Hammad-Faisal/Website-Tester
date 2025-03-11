from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List, Any

from .element import Element

TIMEOUT = 20


class SeleniumElement(Element):
    def goto(self, url: str):
        self.context.get(url)

    def click(self, locator: tuple[str, str]):
        WebDriverWait(self.context, TIMEOUT).until(EC.element_to_be_clickable(locator)).click()

    def set_attribute(self, locator: tuple[str, str], attribute: str, value: str):
        element = WebDriverWait(self.context, TIMEOUT).until(EC.visibility_of_element_located(locator))
        script = f"arguments[0].setAttribute('{attribute}','{value}')"
        self.context.execute_script(script, element)

    def fill(self, locator: tuple[str, str], value: str):
        element = WebDriverWait(self.context, TIMEOUT).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def select_option(self, locator: tuple[str, str], value: str):
        from selenium.webdriver.support.ui import Select
        Select(self.context.find_element(*locator)).select_by_value(value)

    def get_text(self, locator: tuple[str, str]) -> str:
        return self.context.find_element(*locator).text

    def is_visible(self, locator: tuple[str, str]) -> bool:
        try:
            WebDriverWait(self.context, TIMEOUT).until(EC.visibility_of_element_located(locator))
            return self.context.find_element(*locator).is_displayed()
        except Exception:
            return False

    def get_all(self, locator: tuple[str, str]) -> List[Any]:
        return self.context.find_elements(*locator)

    def get_child(self, parent_locator: tuple[str, str], child_locator: tuple) -> 'Element':
        parent = self.context.find_element(*parent_locator)
        child = parent.find_element(*child_locator)
        return SeleniumElement(child)

    def get_all_texts(self, locator: tuple) -> List[str]:
        return [elem.text for elem in self.context.find_elements(*locator)]

    def url(self) -> str:
        return self.context.current_url

    def screenshot(self, path: str):
        self.context.save_screenshot(path)
