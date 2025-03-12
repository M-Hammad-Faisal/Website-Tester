from .browsers import Browser
from src.config import Framework
from .playwright_browsers import (
    get_chrome as playwright_chrome,
    get_firefox as playwright_firefox,
    get_ms_edge as playwright_ms_edge,
)
from .selenium_browsers import (
    get_chrome as selenium_chrome,
    get_firefox as selenium_firefox,
    get_ms_edge as selenium_ms_edge,
)

browsers = {
    Framework.PLAYWRIGHT: {
        Browser.CHROME: playwright_chrome,
        Browser.FIREFOX: playwright_firefox,
        Browser.MSEDGE: playwright_ms_edge,
    },
    Framework.SELENIUM: {
        Browser.CHROME: selenium_chrome,
        Browser.FIREFOX: selenium_firefox,
        Browser.MSEDGE: selenium_ms_edge,
    },
}


def get_browser(framework: Framework, browser: Browser):
    return browsers[framework][browser]
