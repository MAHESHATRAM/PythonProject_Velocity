Flipkart E2E Cart Flow Automation
This project automates an end-to-end cart flow on Flipkart using Selenium WebDriver in Python.
It includes search, product comparison, cart operations, quantity update,
and validation of key messages for a real-world e-commerce workflow.
________________________________________
Features
•	Close login pop-up automatically
•	Search for "mobile" and verify search result text
•	Select 10th and 11th phones for comparison
•	Click on 10th phone to view details
•	Add to cart and verify state change
•	Validate total cart amount
•	Increase product quantity and verify confirmation popup
•	Remove item from cart and verify empty cart message
flipkart_automation/
│
├── tests/
│   └── test_flipkart_flow.py         # High-level E2E test flow
│
├── pages/
│   ├── base_page.py                  # Common driver actions
│   ├── home_page.py                  # Handles search & close login popup
│   ├── search_results_page.py        # Handles compare & select product
│   ├── product_page.py               # Handles add to cart
│   └── cart_page.py                  # Handles cart update, remove, verification
│
├── utils/
│   └── constants.py                  # Stores expected messages/texts
│
├── conftest.py                       # Pytest fixtures for setup/teardown

________________________________________
 How to Run
1. Clone or Download the Repository
Save the script locally as test_flipkart_flow.py.
2. Install Dependencies
Make sure you have Python 3 installed. Then install Selenium:
pip install selenium
3. Setup ChromeDriver
•	Download the matching ChromeDriver: https://chromedriver.chromium.org/downloads
•	Place it in a folder included in your system's PATH
✅ Optional: Use webdriver.Chrome(executable_path='your/path/to/chromedriver') if needed
4. Run the Script
python -m pytest -s .\Test\test_flipkart_workflow.py 
The script will launch Chrome, automate the Flipkart workflow, and print validation results.
________________________________________
🧪 Test Coverage
Test Step	Description
Open Flipkart	Navigate to home page
Close login popup	Skip sign-in modal
Search "mobile"	Enter keyword and verify search result message
Compare 10th & 11th products	Select checkboxes and confirm tray appearance
Click on 10th product	Navigate to product details
Add to cart	Click and verify button state
Cart total	Validate amount consistency
Increase quantity	Validate popup message
Remove product	Confirm removal with popup
Empty cart check	Confirm cart cleared message is visible
________________________________________
 Built With
•	Python 3
•	Selenium WebDriver
•	Google Chrome + ChromeDriver
________________________________________
 Notes
•	This script is for demo/test purposes only. Flipkart may block frequent automated access.
•	UI elements are located using XPath and may change over time.
•	For better structure, consider migrating this logic to a Page Object Model + PyTest suite.
•	Need help or have suggestions? Raise an issue or contact directly.

•   Screenshot embedding instructions
•   Auto-screenshot code in script
•   Test result logging with timestamped filenames
________________________________________


