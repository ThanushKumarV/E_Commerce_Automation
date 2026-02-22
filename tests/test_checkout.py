from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
import allure


def test_add_item_to_cart(setup):
    driver = setup
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    checkout_page = CheckoutPage(driver)

    # 1. Start at Login
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    # 2. Interact with Inventory
    inventory_page.add_backpack_to_cart()

    # 3. Validation
    assert inventory_page.get_cart_count() == "1"

    # 4. Move to next page
    inventory_page.go_to_cart()
    # Now you would initialize CartPage(driver)...

    # 5. click checkout
    checkout_page.click_checkout()
    #6. Enter details
    checkout_page.enter_firstname("Thanush")
    #7 enter lastname
    checkout_page.enter_lastname("Vusa")
    # 8 enter pincode
    checkout_page.enter_pincode('111111')
    # 9 hit contine
    checkout_page.click_continue()
     # assert page title
    Expected = "Checkout: Overview"
    assert checkout_page.page_title() == Expected

    # final submit
    checkout_page.click_finish()
    expected = "Checkout: Complete!"
    assert expected == checkout_page.page_title()








