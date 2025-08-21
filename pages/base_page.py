
"""
This file contains the BasePage class, which is the parent of all page objects.
It contains the basic methods that all page objects will inherit.
"""

from playwright.sync_api import Page

class BasePage:
    """
    The BasePage class is the parent of all page objects.
    It contains the basic methods that all page objects will inherit.
    """

    def __init__(self, page: Page):
        """
        The constructor for the BasePage class.

        :param page: The Playwright page object.
        """
        self.page = page

    def navigate(self, url: str):
        """
        Navigates to the specified URL.

        :param url: The URL to navigate to.
        """
        self.page.goto(url)

    def find_element(self, selector: str):
        """
        Finds an element on the page.

        :param selector: The selector of the element to find.
        :return: The element.
        """
        return self.page.query_selector(selector)

    def click_element(self, selector: str):
        """
        Clicks an element on the page.

        :param selector: The selector of the element to click.
        """
        self.page.click(selector)
