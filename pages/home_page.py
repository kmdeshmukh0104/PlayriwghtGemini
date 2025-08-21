
"""
This file contains the HomePage class, which is the page object for the Playwright home page.
"""

from playwright.sync_api import Page
from pages.base_page import BasePage

class HomePage(BasePage):
    """
    The HomePage class is the page object for the Playwright home page.
    """

    def __init__(self, page: Page):
        """
        The constructor for the HomePage class.

        :param page: The Playwright page object.
        """
        super().__init__(page)
        self.get_started_button = "a.getStarted_Sjon"

    def get_title(self) -> str:
        """
        Gets the title of the page.

        :return: The title of the page.
        """
        return self.page.title()

    def click_get_started_button(self):
        """
        Clicks the "Get started" button.
        """
        self.click_element(self.get_started_button)
