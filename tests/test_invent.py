from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_add_item_to_cart(setup):
    driver = setup
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

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