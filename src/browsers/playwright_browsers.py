from playwright.sync_api import Playwright

from src.config import Config


def get_chrome(context: Playwright):
    return context.chromium.launch(headless=Config.HEADLESS)


def get_firefox(context: Playwright):
    return context.firefox.launch(headless=Config.HEADLESS)


def get_ms_edge(context: Playwright):
    return context.chromium.launch(channel="msedge", headless=Config.HEADLESS)
