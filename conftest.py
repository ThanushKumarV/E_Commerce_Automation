import pytest
from selenium import webdriver
import allure


@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()

    # Disable password manager popup
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)

    # Extra safety options
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs["setup"]
        screenshot = driver.get_screenshot_as_png()
        allure.attach(
            screenshot,
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )