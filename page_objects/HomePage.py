from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.main_handle = self.driver.current_window_handle

    def menu_pricing(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div a:contains('Pricing')")

    def click_menu_pricing(self):
        self.driver.find_element(By.CSS_SELECTOR, "div a[href*='pricing']").click()

    def click_menu_demo(self):
        self.driver.find_element(By.CSS_SELECTOR, "div a[href*='demo']").click()

    def click_btn_get_started(self):
        self.driver.find_element(By.CSS_SELECTOR, "header > div:first-child > div > div:nth-child(2) > a:nth-child(3)").click()
        self._switch_to_new_window()

    def click_btn_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "header > div:first-child > div > div:nth-child(2) > a:nth-child(2)").click()
        self._switch_to_new_window()

    def click_btn_talk_to_sales(self):
        self.driver.find_element(By.CSS_SELECTOR, "header > div:first-child > div > div:nth-child(2) > a:first-child").click()
        self._switch_to_new_window()

    def _switch_to_new_window(self):
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def go_to(self):
        self.driver.get("https://app.phptravels.com")

    def return_to(self):
        self.driver.switch_to.window(self.main_handle)

    def open_sales_iframe_and_wait_ready(self):
        self.click_btn_talk_to_sales()
        iframe = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe")))
        self.driver.switch_to.frame(iframe)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button:contains('15 minutes')")))

    def open_15_min_meeting(self):
        self.open_sales_iframe_and_wait_ready()
        self.driver.find_element(By.CSS_SELECTOR, "button:contains('15 minutes')").click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.calendar-container")))
