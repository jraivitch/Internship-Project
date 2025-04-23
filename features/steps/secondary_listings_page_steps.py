from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC




@when("Verify the page opens")
def verify_page_opens(context):
    context.app.secondary_listings_page.verify_page_opens()


@when("Click on 'filters' button")
def click_filters(context):
    context.app.secondary_listings_page.click_filters_button()

@when("Apply price range filters")
def apply_price_range_filters(context):
   context.app.secondary_listings_page.apply_filters()


@when("Click 'Apply Filter'")
def click_apply_filter_button(context):
    context.app.secondary_listings_page.click_apply_filter_button()