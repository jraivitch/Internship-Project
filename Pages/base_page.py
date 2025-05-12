from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Support.logger import logger

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.target.com/'
        self.wait = WebDriverWait(self.driver, timeout=10)

    def open_url(self, url):
        logger.info(f'Opening {url}')
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)


    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        logger.info(f'Clicking {locator}')
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        logger.info(f'Entering {text}')
        self.driver.find_element(*locator).send_keys(text)

    def wait_until_clickable(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator),
        message=f'Element not clickable: {locator}'
        )

    def wait_until_clickable_click(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator),
        message=f'Element not clickable: {locator}').click()


    def wait_until_visible(self, *locator):
        self.wait.until(EC.visibility_of_element_located(locator),
        message=f'Element not visible: {locator}'
        )

    def wait_until_invisible(self, *locator):
        self.wait.until(EC.invisibility_of_element_located(locator),
        message=f'Element not invisible: {locator}'
        )

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print("Current windows: ", all_windows)
        print("Switching to window: ", all_windows[1])
        self.driver.switch_to.window(all_windows[1])

    def switch_to_window_by_id(self, window_id):
        print("Switching to window: ", window_id)
        self.driver.switch_to.window(window_id)

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, f"{actual_text} != {expected_text}"

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f"{expected_text} not in {actual_text}"

    def verify_partial_url(self, expected_partial_url):
        # current_url = self.driver.current_url
        # assert expected_partial_url in current_url, f"{expected_partial_url} not in {current_url}"
        self.wait.until(EC.url_contains(expected_partial_url),message=f'Expected url {expected_partial_url} not in {expected_partial_url}')

    def verify_url(self, expected_url):
        # current_url = self.driver.current_url
        # assert expected_url == current_url, f"{expected_url} != {current_url}"
        self.wait.until(EC.url_to_be(expected_url),message=f'URL doesn not match {expected_url}')

    def close(self):
        self.driver.close()