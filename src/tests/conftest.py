import pytest
from playwright.sync_api import sync_playwright
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from src.config.framework import Framework
from src.config.config import Config
from src.pages.page import Page
from src.pages.page_factory import PageFactory


def pytest_addoption(parser):
    parser.addoption("--framework", action="store", default=Framework.PLAYWRIGHT,
                     choices=[Framework.PLAYWRIGHT, Framework.SELENIUM],
                     help="Framework: playwright or selenium")


@pytest.fixture(scope="session")
def framework(request):
    return request.config.getoption("--framework")


@pytest.fixture
def pages(framework):
    if framework == Framework.PLAYWRIGHT:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=Config.HEADLESS)
            page = browser.new_page()
            pages = {
                Page.LOGIN: PageFactory.create_page(Page.LOGIN, page, framework),
                Page.INVENTORY: PageFactory.create_page(Page.INVENTORY, page, framework),
                Page.CART: PageFactory.create_page(Page.CART, page, framework),
                Page.CHECKOUT: PageFactory.create_page(Page.CHECKOUT, page, framework)
            }
            yield pages
            browser.close()
    elif framework == Framework.SELENIUM:
        options = Options()
        options.headless = Config.HEADLESS
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.implicitly_wait(5)
        pages = {
            Page.LOGIN: PageFactory.create_page(Page.LOGIN, driver, framework),
            Page.INVENTORY: PageFactory.create_page(Page.INVENTORY, driver, framework),
            Page.CART: PageFactory.create_page(Page.CART, driver, framework),
            Page.CHECKOUT: PageFactory.create_page(Page.CHECKOUT, driver, framework)
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
