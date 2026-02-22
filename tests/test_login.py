from pages.login_page import LoginPage
import allure


@allure.title("Test valid login")
@allure.description("Verify user can login with valid credentials")
def test_valid_login(setup):
    login_page = LoginPage(setup)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    # Assert we moved to the next page
    assert "inventory.html" in setup.current_url

@allure.title("Test invalid login")
@allure.description("Verify user can't login without valid credentials")
def test_invalid_login(setup):
    login_page = LoginPage(setup)
    login_page.load()
    login_page.login("locked_out_user", "secret_sauce")

    # Assert the error message appears
    expected_error = "Epic sadface: Sorry, this user has been locked out."
    assert login_page.get_error_message() == expected_error