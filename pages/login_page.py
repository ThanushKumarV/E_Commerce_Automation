from selenium.webdriver.common.by import By
from utils.base_page import BasePage


class LoginPage(BasePage):
    # --- Locators (The "Map") ---
    # Using Upper Case for constants is a best practice in Python
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    # --- Actions (The "Behaviors") ---

    def load(self):
        """Navigates directly to the SauceDemo login page."""
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        """A high-level 'Flow' method that performs a full login."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        """Returns the text of the error message if login fails."""
        return self.get_text(self.ERROR_MESSAGE)