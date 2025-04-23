from Pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):

    SECONDARY_BUTTON = (By.CSS_SELECTOR, "[href*='/secondary-listings']")

    def click_secondary_option(self):
        self.wait_until_clickable_click(*self.SECONDARY_BUTTON)
