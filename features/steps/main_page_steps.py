from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC




@when("Click 'Secondary' option")
def click_secondary(context):
    context.app.main_page.click_secondary_option()