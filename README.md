# OrangeHRM UI Automation – Playwright (Python)

## Objective

Automate a login flow and perform selected post-login actions on a demo website to demonstrate understanding of:

* UI automation
* Explicit waits and synchronization
* Assertions
* Clean and maintainable test code

---

## Test Website

* **URL:** [https://opensource-demo.orangehrmlive.com/](https://opensource-demo.orangehrmlive.com/)

---

## Tools & Technology Used

* **Automation Tool:** Playwright
* **Programming Language:** Python
* **Browser:** Chromium (Playwright-managed)

---

## Project Overview

This project automates the following workflow on the OrangeHRM demo application:

1. Launches the application in a browser with a maximized window.
2. Logs in using provided credentials.
3. Verifies successful login using a dashboard assertion.
4. Performs two post-login actions with validations:

   * Navigate to **PIM → Add Employee** and enter employee details.
   * Navigate to **My Info** and verify the Personal Details section.
5. Handles basic exceptions and captures screenshots on failures.

---

## Automated Scenarios

### 1. Application Launch

* Opens the OrangeHRM demo website.
* Uses a maximized viewport (1920x1080).
* Applies explicit waits to ensure elements are loaded before interaction.

### 2. Login Automation

* Logs in using the following credentials:

  * **Username:** Admin
  * **Password:** admin123
* **Assertion:** Verifies successful login by checking the visibility and text of the *Dashboard* heading.

### 3. Post-Login Actions

#### Action 1: PIM → Add Employee

* Navigates to the PIM module.
* Opens the Add Employee page.
* Enters First Name and Last Name.
* **Assertion:** Confirms the visibility of the *Add Employee* page heading.

#### Action 2: My Info

* Navigates to the My Info section.
* **Assertion:** Confirms the visibility of the *Personal Details* section header.

---

## Code Quality & Best Practices Followed

* Uses **stable CSS and text-based locators** (avoids absolute XPaths).
* Implements **explicit waits** (`wait_for_selector`) instead of hard-coded delays.
* Includes **meaningful assertions** after each critical step.
* Maintains **clean, readable, and well-commented code**.
* Handles **TimeoutError** and **AssertionError** with screenshots for debugging.

---

## Project Structure

```
.
├── test_orangehrm.py      # Main Playwright automation script
├── README.md             # Project documentation
├── timeout_error.png     # Screenshot (generated on timeout failure)
├── assertion_error.png   # Screenshot (generated on assertion failure)
```

---

## Steps to Run the Automation

### Prerequisites

* Python 3.8 or above installed
* Pip package manager available

### Installation

```bash
pip install playwright
playwright install
```

### Execute the Test

```bash
python test_orangehrm.py
```

---

## Expected Outcome

* Browser launches and logs into the OrangeHRM application successfully.
* PIM → Add Employee page is validated and employee details are entered.
* My Info page is opened and verified.
* Screenshots are captured automatically if any timeout or assertion failure occurs.
