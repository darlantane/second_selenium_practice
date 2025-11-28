from selenium.webdriver.common.by import By
from HomePage import HomePage

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


class IntegrationPage(HomePage):
    URL = "https://phptravels.com/integrations/"

    FILTERS = {
        "Flights": (By.LINK_TEXT, "Flights"),
        "Hotels": (By.LINK_TEXT, "Hotels"),
        "Tours": (By.LINK_TEXT, "Tours"),
        "Cars": (By.LINK_TEXT, "Cars"),
        "Payment Gateway": (By.LINK_TEXT, "Payment Gateway"),
        "All": (By.LINK_TEXT, "All Suppliers"),
    }

    TILE_LOCATOR = (By.CSS_SELECTOR, "div.col-md-3")

    def open_page(self):
        self.open(self.URL)

    def apply_filter(self, name):
        self.click(self.FILTERS[name])

    def tiles(self):
        elements = self.finds(self.TILE_LOCATOR)
        return [IntegrationTile(e) for e in elements]
