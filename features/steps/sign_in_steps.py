from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@given("Open Reely main page")
def open_main_page(context):
    context.app.login_page.open_main_login_page()


@when("Enter email and password")
def enter_credentials(context):
    context.app.login_page.input_username()
    context.app.login_page.input_password()


@when("Click continue")
def click_continue(context):
    context.app.login_page.click_continue_button()




