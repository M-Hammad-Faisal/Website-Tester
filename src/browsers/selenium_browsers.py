from src.config import Config

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions


def get_chrome():
    options = ChromeOptions()
    options.headless = Config.HEADLESS
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--headless") if Config.HEADLESS else None
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


def get_firefox():
    options = FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    options.add_argument("--headless") if Config.HEADLESS else None
    return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)


def get_ms_edge():
    options = EdgeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--headless") if Config.HEADLESS else None
    return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
