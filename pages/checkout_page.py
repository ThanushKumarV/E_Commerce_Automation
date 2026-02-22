from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class CheckoutPage(BasePage):
    CART_ICON = (By.XPATH,"//a[@class='shopping_cart_link']")
    CHECKOUT = (By.ID,"checkout")
    CHECKOUT_USER =(By.ID,"first-name")
    CHECKOUT_LAST_NAME =(By.ID,"last-name")
    PINCODE = (By.ID,"postal-code")
    CONTINUE = (By.ID,"continue")
    PAGE_TITLE = (By.CLASS_NAME, "title")
    SUBMIT_BTN = (By.ID,"finish")

    # ACTIONS
    def go_to_cart(self):
        """Navigates to the Cart page."""
        self.click(self.CART_ICON)
    def click_checkout(self):
        self.click(self.CHECKOUT)
    def enter_firstname(self,firstname):
        self.enter_text(self.CHECKOUT_USER,firstname)
    def enter_lastname(self,lastname):
        self.enter_text(self.CHECKOUT_LAST_NAME,lastname)
    def enter_pincode(self,code):
        self.enter_text(self.PINCODE,code)
    def click_continue(self):
        self.click(self.CONTINUE)
    def page_title(self):
        return self.get_text(self.PAGE_TITLE)
    def click_finish(self):
        self.click(self.SUBMIT_BTN)


