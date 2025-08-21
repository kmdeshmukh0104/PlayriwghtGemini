
"""
This file contains an example test case.
"""

import pytest
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage
from config import BASE_URL

@pytest.fixture(scope="module")
def browser():
    """
    The browser fixture.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    """
    The page fixture.
    """
    page = browser.new_page()
    yield page
    page.close()

def test_example(page):
    """
    An example test case.

    :param page: The Playwright page object.
    """
    home_page = HomePage(page)
    home_page.navigate(BASE_URL)
    assert "Playwright" in home_page.get_title()
    home_page.click_get_started_button()
    assert page.url == f"{BASE_URL}docs/intro"
