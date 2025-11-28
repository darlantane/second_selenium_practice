from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class PricingPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)
        self.main_handle = self.driver.current_window_handle

    def go_to(self):
        self.driver.get('https://phptravels.com/pricing')

    def texte_titre(self):
        return self.driver.find_element(By.CSS_SELECTOR, "h1")

    def texte_explicatif(self):
        return self.driver.find_element(By.XPATH, "//h1/../p")

    def return_to(self):
        self.driver.switch_to.window(self.main_handle)