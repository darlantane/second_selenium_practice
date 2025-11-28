from selenium.webdriver.common.by import By

class IntegrationTile:

    def __init__(self, root):
        self.root = root

    def image(self):
        return self.root.find_element(By.TAG_NAME, "img")

    def title(self):
        return self.root.find_element(By.TAG_NAME, "h4").text.strip()

    def supplier_type(self):
        return self.root.find_element(By.CLASS_NAME, "supplier-type").text.strip()

    def body_text(self):
        return self.root.find_element(By.CLASS_NAME, "text").text.strip()

    def view_details(self):
        return self.root.find_element(By.LINK_TEXT, "View Details")

    def tooltip(self):
        return self.root.get_attribute("data-original-title")