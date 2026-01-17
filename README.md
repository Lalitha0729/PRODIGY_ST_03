# PRODIGY_ST_03
Test Suite for a website to automate login functionality testing , Task 3
**Task 3 - Automated Login Testing – SauceDemo Website**
**Project Overview**

This project demonstrates automated testing of the login functionality for a web application using Selenium WebDriver with Python.
The target application under test is the SauceDemo website, which is commonly used for practicing test automation.

**The automation suite covers:**

1 Positive login scenarios (valid credentials)

2 Negative login scenarios (invalid credentials, locked user)

3 Edge cases (empty input fields)

4 Screenshot capture for execution evidence

**Application Under Test (AUT)**

Application Name: SauceDemo

URL: https://www.saucedemo.com/

Type: Web-based E-commerce Demo Application

Login Credentials:

Password for all users: secret_sauce

Accepted Usernames

standard_user

locked_out_user

problem_user

performance_glitch_user

error_user

visual_user

**Objectives**

*Automate login functionality testing

*Validate successful login for valid users

*Verify error handling for invalid login attempts

*Capture screenshots for proof of test execution

*Follow industry-standard automation practices

**Test Scenarios Covered**
✅ Positive Test Cases

1 Login using valid usernames with correct password

2 Verify successful navigation to inventory page

❌ Negative Test Cases

1 Login with locked user

2 Login with wrong password

3 Login with empty username and password fields

**Tools & Technologies Used**

Programming Language: Python

Automation Tool: Selenium WebDriver

Browser: Google Chrome

IDE: VS Code

Version Control: Git & GitHub

**Prerequisites**

Ensure the following are installed before running the script:

1 Python 3.x

2 Google Chrome Browser

3 ChromeDriver (compatible with your Chrome version)

4 Selenium library

5 Install Selenium using:

6 pip install selenium

📂 Project Structure
saucedemo-login-automation/
│
├── Test_Suite.py
├── screenshots/
│   ├── standard_user_login.png
│   ├── locked_out_user_login.png
│   ├── problem_user_login.png
│   ├── visual_user_login.png
│
└── README.md

**How to Execute the Test**

1.Clone the repository

2.git clone <repository-url>

3.Navigate to the project folder

4.cd saucedemo-login-automation

5.Run the test script

python login_test.py

**Screenshot Evidence**

Screenshots are automatically captured during execution for:

 1.Successful logins

 2.Error messages

 3.Empty field validation

These screenshots act as proof of execution and help in debugging failures.

**Key Learnings**

1.Selenium WebDriver automation basics

2.Handling positive and negative test cases

3.Screenshot capturing for test evidence

4.Web element interaction using locators

5.Industry-standard automation practices

**Conclusion**

The automated login test suite successfully validates the login functionality of the SauceDemo application.
All scenarios were executed and verified with proper logging and screenshots, ensuring reliability and test coverage.

👤 Author

Name: Lalitha B
