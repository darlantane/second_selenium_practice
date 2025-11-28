from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TalkToSalesPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)
        self.main_handle = self.driver.current_window_handle

    def switch_to_frame(self):
        self.wait.until(expected_conditions.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, "main > div > div > iframe")))

    def frame_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[@data-id='dossier'] > div > h1")

    def frame_text_welcome(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[@data-id='dossier'] > div[2]")

    def fifteen_minute_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[@data-id='event-type-header-title']")

    def click_fifteen_minute_button(self):
        self.fifteen_minute_button().click()
        self.driver.switch_to.default_content()
        self.wait.until(expected_conditions.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe")))

    def calendar_displays(self):
        return self.wait.until(expected_conditions.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe")))

    def return_to(self):
        self.driver.switch_to.window(self.main_handle)