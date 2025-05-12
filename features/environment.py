from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from app.application import Application
from Support.logger import logger

def browser_init(context, browser="chrome", headless=False, mobile_emulation=True):
    """
    :param context: Behave context
    :param browser: 'chrome' or 'firefox'
    :param headless: True to run headless
    :param mobile_emulation: True to enable Chrome mobile emulation
    """

    if browser == "chrome":
        options = webdriver.ChromeOptions()

        if mobile_emulation:
            mobile_device = "iPhone X"  # or 'Pixel 5', 'Galaxy S5', etc.
            options.add_experimental_option("mobileEmulation", {"deviceName": mobile_device})

        if headless:
            options.add_argument('--headless=new')
            options.add_argument('--disable-gpu')
            if not mobile_emulation:
                options.add_argument('--window-size=1920,1080')
            else:
                options.add_argument('--window-size=375,812')  # Mobile size (iPhone X)

        service = ChromeService(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service, options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.headless = True
        service = FirefoxService(GeckoDriverManager().install())
        context.driver = webdriver.Firefox(service=service, options=options)

    else:
        raise Exception(f"Unsupported browser: {browser}")

    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario:', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')

    # Toggle mobile_emulation and headless as needed
    browser_init(context, browser="chrome", headless=False, mobile_emulation=True)

def before_step(context, step):
    logger.info(f'Started step: {step.name}')
    print('\nStarted step:', step)

def after_step(context, step):
    if step.status == 'failed':
        logger.warning(f'Step failed with status: {step}')
        print('\nStep failed:', step)

def after_scenario(context, scenario):
    context.driver.quit()
