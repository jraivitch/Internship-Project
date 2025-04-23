from Pages.base_page import Page
from Pages.main_page import MainPage
from Pages.login_page import LoginPage
from Pages.secondary_listings_page import SecondaryListingsPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.secondary_listings_page = SecondaryListingsPage(driver)
