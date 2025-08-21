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
        self.search_button = "button.DocSearch-Button"
        self.search_input = "input.DocSearch-Input"
        self.docs_link = "a[href='/docs/intro']"
        self.api_link = "a[href='/docs/api/class-playwright']"
        self.theme_toggle = "button.colorModeToggle_DEke"
        self.language_dropdown = "div.navbar__item.dropdown--hoverable"
        self.search_results_modal = "div.DocSearch-Modal"

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

    def search(self, text: str):
        """
        Searches for the specified text.

        :param text: The text to search for.
        """
        self.click_element(self.search_button)
        self.page.fill(self.search_input, text)
        self.page.press(self.search_input, "Enter")

    def is_search_results_modal_visible(self) -> bool:
        """
        Checks if the search results modal is visible.

        :return: True if the search results modal is visible, False otherwise.
        """
        return self.page.is_visible(self.search_results_modal)

    def click_docs_link(self):
        """
        Clicks the "Docs" link.
        """
        self.click_element(self.docs_link)

    def click_api_link(self):
        """
        Clicks the "API" link.
        """
        self.click_element(self.api_link)

    def get_theme(self) -> str:
        """
        Gets the current theme.

        :return: The current theme.
        """
        print(f"Current theme: {self.page.locator('html').get_attribute('data-theme')}")
        return self.page.locator("html").get_attribute("data-theme")

    def toggle_theme(self):
        """
        Toggles the theme.
        """
        for _ in range(3):
            try:
                self.click_element(self.theme_toggle)
                self.page.wait_for_timeout(1000)
                break
            except:
                pass

    def select_language(self, language: str):
        """
        Selects the specified language from the dropdown.

        :param language: The language to select.
        """
        self.click_element(self.language_dropdown)
        self.page.click(f"a:text('{language}')")