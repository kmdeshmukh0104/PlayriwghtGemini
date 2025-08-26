
import sys
from os.path import abspath, dirname
import pytest
from playwright.sync_api import sync_playwright

# Add the project root directory to the Python path
sys.path.insert(0, dirname(abspath(__file__)))

# conftest.py


def pytest_addoption(parser):
    parser.addoption(
        "--headless", action="store_true", default=False, help="Run browser in headless mode"
    )

@pytest.fixture(scope="session")
def browser(request):
    headless = request.config.getoption("--headless")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        yield browser
        browser.close()
