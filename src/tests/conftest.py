import pytest

from playwright.sync_api import sync_playwright

from src.config.framework import Framework
from src.pages.page import Page
from src.pages.page_factory import PageFactory
from src.browsers import Browser, get_browser


def pytest_addoption(parser):
    parser.addoption(
        "--framework",
        action="store",
        default=Framework.PLAYWRIGHT,
        help=f"Framework: {Framework.PLAYWRIGHT} or {Framework.SELENIUM}",
    )
    parser.addoption(
        "--browser",
        action="store",
        default=Browser.CHROME,
        help=f"Browser: {Browser.CHROME}, {Browser.FIREFOX}, or {Browser.MSEDGE}",
    )


@pytest.fixture(scope="function")
def framework(request):
    return request.config.getoption("--framework")


@pytest.fixture(scope="function")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="function")
def pages(framework, browser):
    if framework == Framework.PLAYWRIGHT:
        with sync_playwright() as p:
            browser = get_browser(framework, browser)(p)
            page = browser.new_page()
            pages = {
                Page.LOGIN: PageFactory.create_page(Page.LOGIN, page, framework),
                Page.INVENTORY: PageFactory.create_page(Page.INVENTORY, page, framework),
                Page.CART: PageFactory.create_page(Page.CART, page, framework),
                Page.CHECKOUT: PageFactory.create_page(Page.CHECKOUT, page, framework),
            }
            yield pages
            browser.close()
    elif framework == Framework.SELENIUM:
        driver = get_browser(framework, browser)()
        driver.implicitly_wait(5)
        pages = {
            Page.LOGIN: PageFactory.create_page(Page.LOGIN, driver, framework),
            Page.INVENTORY: PageFactory.create_page(Page.INVENTORY, driver, framework),
            Page.CART: PageFactory.create_page(Page.CART, driver, framework),
            Page.CHECKOUT: PageFactory.create_page(Page.CHECKOUT, driver, framework),
        }
        yield pages
        driver.quit()


@pytest.fixture
def login_as_standard_user(pages):
    login_page, inventory_page = pages[Page.LOGIN], pages[Page.INVENTORY]
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    assert inventory_page.is_loaded(), "Login failed"
    return pages
