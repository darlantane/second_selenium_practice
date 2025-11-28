from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class DemoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)
        self.main_handle = self.driver.current_window_handle

    def text_intitule(self):
        return self.driver.find_element(By.CSS_SELECTOR, "main > section.pricing-section > div > div > div:first-of-type h2")

    def input_first_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, "main > section:nth-of-type(2) input[type='text']:nth-of-type(1)")

    def input_last_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, "main > section:nth-of-type(2) input[type='text']:nth-of-type(2)")

    def input_email(self):
        return self.driver.find_element(By.CSS_SELECTOR, "main > section:nth-of-type(2) input[type='email']")

    def input_business_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, "main > section:nth-of-type(2) input[type='text']:nth-of-type(3)")

    def input_whatsapp_number(self):
        return self.driver.find_element(By.CSS_SELECTOR, "main > section:nth-of-type(2) input[type='tel']")

    def input_result(self):
        return self.driver.find_element(By.ID, 'number')

    def click_btn_submit(self):
        self.driver.find_element(By.ID, 'demo').click()

    def get_alert(self):
        return self.wait.until(expected_conditions.alert_is_present())

    def fill_form(self, first_name, last_name, email, business_name, whatsapp_number, result):
        self.input_first_name().send_keys(first_name)
        self.input_last_name().send_keys(last_name)
        self.input_email().send_keys(email)
        self.input_business_name().send_keys(business_name)
        self.input_whatsapp_number().send_keys(whatsapp_number)
        self.input_result().send_keys(result)
        self.click_btn_submit()