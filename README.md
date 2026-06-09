# Test Automation Project – Urban Routes
 
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green?logo=selenium)
![Pytest](https://img.shields.io/badge/Pytest-Framework-orange?logo=pytest)
 
## Objective
 
Design, implement, and execute automated end-to-end tests for the Urban Routes web application, validating the complete ride-booking workflow using Python, Selenium WebDriver, and the Page Object Model (POM) design pattern.
 
---
 
## Project Structure
 
```
Urban_Routes/
├── main.py       # Test class with all 8 automated test cases
├── pages.py      # Page Object Model — UI interactions and locators
├── data.py       # Centralized test data and environment config
└── helpers.py    # Utility functions (URL check, SMS code retrieval)
```
 
---
 
## Test Suite Overview
 
All tests are organized in a single `TestUrbanRoutes` class using Pytest, with `setup_class` initializing the Chrome driver and `teardown_class` closing the session.
 
```python
class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
 
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to Urban Routes server.")
        else:
            print("Could not connect. Please check if the server is running.")
```
 
---
 
## Test Cases
 
| # | Test | Method | Assertion |
|---|---|---|---|
| 1 | Set route addresses | `test_set_route` | Origin and destination fields match test data |
| 2 | Select Comfort plan | `test_select_plan` | Comfort plan is active |
| 3 | Register phone number | `test_fill_phone_number` | Phone confirmed via SMS code |
| 4 | Add credit card | `test_fill_card` | Card successfully added |
| 5 | Write driver comment | `test_comment_for_driver` | Comment matches input value |
| 6 | Request blanket & tissues | `test_order_toggle_blanket_and_tissues` | Toggle is active |
| 7 | Order 2 ice creams | `test_order_2_ice_creams` | Counter equals 2 |
| 8 | Submit ride & search vehicle | `test_car_search_model_appears` | Search modal is visible |
 
### Example — Ice Cream Order Test
 
```python
def test_order_2_ice_creams(self):
    self.page.open_comfort_flow()
    self.page.add_ice_cream(2)
 
    assert self.page.get_ice_cream_count() == 2
```
 
### Example — Full End-to-End Ride Request
 
```python
def test_car_search_model_appears(self):
    self.page.open_comfort_flow()
    self.page.fill_phone_flow(data.PHONE_NUMBER)
    code = helpers.retrieve_phone_code(self.driver)
    self.page.fill_code(code)
    self.page.confirm_code()
    self.page.complete_payment_flow(data.CARD_NUMBER, data.CARD_CODE)
    self.page.add_comment(data.MESSAGE_FOR_DRIVER)
    self.page.add_ice_cream(2)
    self.page.toggle_blanket_and_tissues()
    self.page.click_order_button()
 
    assert self.page.is_search_car_visible()
```
 
---
 
## Test Data Configuration
 
All test inputs are centralized in `data.py`, keeping test logic clean and easy to maintain:
 
```python
URBAN_ROUTES_URL = 'https://...'
ADDRESS_FROM     = 'East 2nd Street, 601'
ADDRESS_TO       = '1300 1st St'
PHONE_NUMBER     = '+1 123 123 12 12'
CARD_NUMBER      = '1234 5678 9100'
CARD_CODE        = '1111'
MESSAGE_FOR_DRIVER = 'Pare no bar de sucos'
```
 
---
 
## How to Run
 
```bash
# 1. Clone the repository
git clone https://github.com/priscila-venske/Test_Automation_Project-Urban_Routes.git
cd Test_Automation_Project-Urban_Routes
 
# 2. Install dependencies
pip install selenium pytest
 
# 3. Make sure the Urban Routes server is running, then execute
pytest main.py -v
```
 
---
 
## Architecture — Page Object Model
 
The POM pattern separates test logic (`main.py`) from UI interaction logic (`pages.py`), making the suite easier to maintain when the UI changes — only the page class needs updating, not the tests themselves.
 
```
Test logic (main.py)
    └── calls → Page methods (pages.py)
                    └── uses → Selenium locators + WebDriver actions
```
 
---
 
## Technologies Used
 
| Tool | Purpose |
|---|---|
| Python | Test scripting language |
| Selenium WebDriver | Browser automation |
| Pytest | Test runner and assertions |
| ChromeDriver | Chrome browser control |
| Git / GitHub | Version control |
 
---
 
## Author
 
Project developed as part of the **QA Engineering Bootcamp** at TripleTen.
 
