"""
This file contains the RagistrationPage class, which is the page object for the Playwright home page.
"""

import re
from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.common_functions import CommonFunctions
from playwright.sync_api import expect

class RagistrationPage(BasePage):
    """
    The RagistrationPage class is the page object for the Playwright home page.
    """

    random_user = CommonFunctions.random_string()
    def __init__(self, page: Page):
        """
        The constructor for the RagistrationPage class.

        :param page: The Playwright page object.
        """
        super().__init__(page)

    def get_title(self) -> str:
        """
        Gets the title of the page.

        :return: The title of the page.
        """
        return self.page.title()
    
    def expect_title_contains(self, text: str):
        """Use Playwright expect to check partial match in title"""
        expect(self.page).to_have_title(re.compile(text))
    
    def expect_title_is(self, text: str):
        """Use Playwright expect to check exact title"""
        expect(self.page).to_have_title(text)


    def enter_email(self):
        """
        Clicks the "Get started" button.
        """
        email = self.random_user + "@gmail.com"
        print(email)
        self.page.get_by_role("textbox", name="Email").fill(email)
    
    def enter_username(self):
        """
        Clicks the "Get started" button.
        """
        self.page.get_by_role("textbox", name="Username").fill(self.random_user)

    def enter_password(self):
        """
        Clicks the "Get started" button.
        """
        self.page.get_by_role("textbox", name="Password").fill("test@123")

    def click_signup_button(self):
        """
        Clicks the "Get started" button.
        """
        self.page.get_by_role("button", name="Sign up").click()

    # def search(self, text: str):
    #     """
    #     Searches for the specified text.

    #     :param text: The text to search for.
    #     """
    #     self.click_element(self.search_button)
    #     self.page.fill(self.search_input, text)
    #     self.page.press(self.search_input, "Enter")

    # def is_search_results_modal_visible(self) -> bool:
    #     """
    #     Checks if the search results modal is visible.

    #     :return: True if the search results modal is visible, False otherwise.
    #     """
    #     return self.page.is_visible(self.search_results_modal)

    # def click_docs_link(self):
    #     """
    #     Clicks the "Docs" link.
    #     """
    #     self.click_element(self.docs_link)

    # def click_api_link(self):
    #     """
    #     Clicks the "API" link.
    #     """
    #     self.click_element(self.api_link)

    # def get_theme(self) -> str:
    #     """
    #     Gets the current theme.

    #     :return: The current theme.
    #     """
    #     print(f"Current theme: {self.page.locator('html').get_attribute('data-theme')}")
    #     return self.page.locator("html").get_attribute("data-theme")

    # def toggle_theme(self):
    #     """
    #     Toggles the theme.
    #     """
    #     for _ in range(3):
    #         try:
    #             self.click_element(self.theme_toggle)
    #             self.page.wait_for_timeout(1000)
    #             break
    #         except:
    #             pass

    # def select_language(self, language: str):
    #     """
    #     Selects the specified language from the dropdown.

    #     :param language: The language to select.
    #     """
    #     self.click_element(self.language_dropdown)
    #     self.page.click(f"a:text('{language}')")