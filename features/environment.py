from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from app.application import Application
from Support.logger import logger

def browser_init(context, browser="chrome", headless=False):
    """
    :param context: Behave context
    :param browser: 'chrome' or 'firefox'
    :param headless: True to run headless
    """

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless=new')  # For Chrome v109+
            options.add_argument('--disable-gpu')
            options.add_argument('--window-size=1920,1080')
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

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)

    # ##BROWSERSTACK CONFIGS#####
    # USERNAME = "jordanraivitch_lvOHgx"
    # ACCESS_KEY = "UVKDzSyHHQqZAPP7JLBW"
    #
    # BROWSERSTACK_URL = f"http://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"
    #
    # # ✅ Set desired capabilities using Options
    # options = webdriver.ChromeOptions()
    # options.set_capability('os', 'Windows')
    # options.set_capability('os_version', '11')
    # options.set_capability('browser', 'Chrome')
    # options.set_capability('browser_version', 'latest')
    # options.set_capability('name', 'Behave Test - Chrome on Windows')
    # options.set_capability('build', 'Behave Tests Build 1')
    # options.set_capability('browserstack.debug', True)
    # options.set_capability('browserstack.console', 'errors')
    # options.set_capability('browserstack.networkLogs', True)
    #
    # # ✅ Start remote driver with options
    # context.driver = webdriver.Remote(
    #     command_executor=BROWSERSTACK_URL,
    #     options=options
    # )
    #
    # context.driver.implicitly_wait(10)
    # context.driver.maximize_window()
    # context.wait = WebDriverWait(context.driver, timeout=10)
    # context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario:', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    # Set your desired config here:
    browser_init(context, browser="chrome", headless=False)


def before_step(context, step):
    logger.info(f'Started step: {step.name}')
    print('\nStarted step:', step)


def after_step(context, step):
    if step.status == 'failed':
        logger.warning(f'Step failed with status: {step}')
        print('\nStep failed:', step)


def after_scenario(context, scenario):
    context.driver.quit()
