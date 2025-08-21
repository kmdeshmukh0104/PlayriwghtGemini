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

def test_search(page):
    """
    Tests the search functionality.

    :param page: The Playwright page object.
    """
    home_page = HomePage(page)
    home_page.navigate(BASE_URL)
    home_page.search("testing")
    assert home_page.is_search_results_modal_visible()

def test_navigation_links(page):
    """
    Tests the navigation links.

    :param page: The Playwright page object.
    """
    home_page = HomePage(page)
    home_page.navigate(BASE_URL)
    home_page.click_docs_link()
    assert page.url == f"{BASE_URL}docs/intro"
    home_page.click_api_link()
    assert page.url == f"{BASE_URL}docs/api/class-playwright"

@pytest.mark.skip(reason="Theme toggle not working in test environment")
def test_theme_toggle(page):
    """
    Tests the theme toggle.

    :param page: The Playwright page object.
    """
    home_page = HomePage(page)
    home_page.navigate(BASE_URL)
    home_page.page.wait_for_load_state("networkidle")
    initial_theme = home_page.get_theme()
    home_page.toggle_theme()
    new_theme = home_page.get_theme()
    assert initial_theme != new_theme

def test_language_dropdown(page):
    """
    Tests the language dropdown.

    :param page: The Playwright page object.
    """
    home_page = HomePage(page)
    home_page.navigate(BASE_URL)
    home_page.select_language("Python")
    assert "python" in page.url