from time import sleep

from Pages.base_page import Page
from selenium.webdriver.common.by import By

class SecondaryListingsPage(Page):
    FILTERS_BUTTON = (By.CSS_SELECTOR, "[class='filter-button']")
    RANGE_FROM = (By.CSS_SELECTOR, 'input[wized="unitPriceFromFilter"]')
    RANGE_TO = (By.CSS_SELECTOR, 'input[wized="unitPriceToFilter"]')
    APPLY_FILTER_BTN = (By.CSS_SELECTOR, 'a[wized="applyFilterButtonMLS"]')

    def verify_page_opens(self):
        self.verify_url("https://soft.reelly.io/secondary-listings")


    def click_filters_button(self):
        self.wait_until_clickable_click(*self.FILTERS_BUTTON)
        self.wait_until_clickable_click(*self.FILTERS_BUTTON)
        print("Button clicked")
        sleep(4)

    def apply_filters(self):

        self.wait_until_visible(*self.RANGE_FROM)
        self.input_text("120000", *self.RANGE_FROM)

        self.wait_until_visible(*self.RANGE_TO)
        self.input_text("200000", *self.RANGE_TO)


    def click_apply_filter_button(self):
        self.wait_until_clickable_click(*self.APPLY_FILTER_BTN)

    #
    # def verify_prices_in_range(self):
