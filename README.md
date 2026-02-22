🛒 E-Commerce Automation Framework (Selenium + Pytest + Allure)
📌 Project Overview

This project is a Selenium automation framework built using:

Python
Selenium WebDriver
Pytest
Page Object Model (POM)
Allure Reporting
Logging

The framework automates an e-commerce application including login, inventory, cart, and checkout flows.
It is designed to be scalable, reusable, and maintainable, following industry best practices.

🏗️ Framework Architecture

The framework follows the Page Object Model (POM) design pattern.
e-commerce automation/
│
├── pages/              # Page classes (POM)
│   ├── login_page.py
│   ├── inventory_page.py
│   └── checkout_page.py
│
├── tests/              # Test cases
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_checkout.py
│
├── utils/              # Utilities
│   ├── base_page.py
│   ├── logger.py
│   └── config.py
│
├── test_data/          # Test data (JSON)
│   └── test_users.json
│
├── logs/               # Execution logs
├── reports/            # Allure report files
├── conftest.py         # Fixtures & hooks
└── requirements.txt

🚀 Key Features
✅ Page Object Model (POM)
Separates locators and actions
Improves maintainability
Reduces code duplication

✅ Pytest Fixtures
Centralized WebDriver setup & teardown
Clean test methods

✅ Automatic Screenshot on Failure
Uses pytest_runtest_makereport hook
Captures screenshot only when test fails
Screenshot attached to Allure report

✅ Allure Reporting
Detailed HTML report
Step-level execution
Failure screenshots
Execution time tracking

✅ Logging
Centralized logging system
Timestamp-based log files
Helps debugging failures

🧠 Screenshot Handling Logic
The framework automatically captures screenshots when a test fails.
It works by:
Intercepting test results using Pytest hook
Checking if the test failed during execution phase
Fetching WebDriver instance from fixture
Capturing screenshot as PNG
Attaching screenshot to Allure report
This avoids writing screenshot code inside every test.

⚙️ Installation
1️⃣ Clone the repository
git clone <https://github.com/ThanushKumarV/E_Commerce_Automation.git>
cd e-commerce-automation
2️⃣ Create virtual environment
python -m venv .venv

Activate:
Windows:
.venv\Scripts\activate
Mac/Linux:
source .venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ How to Run Tests
Run all tests:
pytest
Run with Allure report:
pytest --alluredir=reports
Generate Allure HTML report:
allure serve reports

🧪 Sample Test Flow
Login with valid user
Add product to cart
Navigate to cart
Complete checkout process
Verify successful order placement

🔧 Technologies Used
Python
Selenium WebDriver
Pytest
Allure Reporting
Logging module
JSON for test data
