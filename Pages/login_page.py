from Pages.base_page import Page
from selenium.webdriver.common.by import By

class LoginPage(Page):

    EMAIL_BOX = (By.ID, "email-2")
    PASSWORD_BOX = (By.ID, "field")
    CONTINUE_BOX = (By.CSS_SELECTOR, "[class*='login-button']")

    def open_main_login_page(self):
        self.open_url("https://soft.reelly.io/sign-in")

    def input_username(self):
        self.wait_until_visible(*self.EMAIL_BOX)
        self.input_text("jraivitch@gmail.com", *self.EMAIL_BOX)

    def input_password(self):
        self.wait_until_visible(*self.PASSWORD_BOX)
        self.input_text("Hawaii2015!!!!", *self.PASSWORD_BOX)

    def click_continue_button(self):
        self.wait_until_clickable_click(*self.CONTINUE_BOX)