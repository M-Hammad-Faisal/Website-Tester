from abc import ABC, abstractmethod
from typing import Union, List, Any


class Element(ABC):
    def __init__(self, context: Any):
        self.context = context

    @abstractmethod
    def goto(self, url: str):
        pass

    @abstractmethod
    def click(self, locator: Union[str, tuple]):
        pass

    @abstractmethod
    def fill(self, locator: Union[str, tuple], value: str):
        pass

    @abstractmethod
    def set_attribute(self, locator: Union[str, tuple], attribute: str, value: str):
        pass

    @abstractmethod
    def select_option(self, locator: Union[str, tuple], value: str):
        pass

    @abstractmethod
    def get_text(self, locator: Union[str, tuple]) -> str:
        pass

    @abstractmethod
    def is_visible(self, locator: Union[str, tuple]) -> bool:
        pass

    @abstractmethod
    def get_all(self, locator: Union[str, tuple]) -> List[Any]:
        pass

    @abstractmethod
    def get_child(self, parent_locator: Union[str, tuple], child_locator: Union[str, tuple]) -> 'Element':
        pass

    @abstractmethod
    def get_all_texts(self, locator: Union[str, tuple]) -> List[str]:
        pass

    @abstractmethod
    def url(self) -> str:
        pass

    @abstractmethod
    def screenshot(self, path: str):
        pass


class ElementFactory:
    @staticmethod
    def create_element(framework: str, context: Any) -> Element:
        from src.config.framework import Framework

        if framework == Framework.PLAYWRIGHT:
            from src.config.framework import PlaywrightElement
            return PlaywrightElement(context)

        elif framework == Framework.SELENIUM:
            from src.config.framework import SeleniumElement
            return SeleniumElement(context)

        raise ValueError(f"Unsupported framework: {framework}")
