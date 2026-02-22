from selenium.webdriver.common.by import By
from utils.base_page import BasePage


class InventoryPage(BasePage):
    # --- Locators ---
    # It's better to name specific items clearly
    BACKPACK_ADD_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    BIKE_LIGHT_ADD_BTN = (By.ID, "add-to-cart-sauce-labs-bike-light")

    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    PAGE_TITLE = (By.CLASS_NAME, "title")

    # --- Actions ---

    def get_title(self):
        """Returns 'Products' to verify we logged in successfully."""
        return self.get_text(self.PAGE_TITLE)

    def add_backpack_to_cart(self):
        self.click(self.BACKPACK_ADD_BTN)

    def get_cart_count(self):
        """Returns the number shown on the shopping cart badge."""
        return self.get_text(self.CART_BADGE)

    def go_to_cart(self):
        """Navigates to the Cart page."""
        self.click(self.CART_ICON)