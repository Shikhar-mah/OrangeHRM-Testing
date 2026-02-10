# Import Playwright sync API and TimeoutError for exception handling
from playwright.sync_api import sync_playwright, TimeoutError

# ----------------------------
# Test Configuration
# ----------------------------

# Application URL (OrangeHRM demo site)
URL = "https://opensource-demo.orangehrmlive.com/"

# Login credentials provided by the assignment
USERNAME = "Admin"
PASSWORD = "admin123"


def test_orangehrm():
    """
    Objective:
    Automate login and perform post-login actions on the OrangeHRM demo site
    to demonstrate UI automation, synchronization, and assertions.
    """

    # Launch Playwright in synchronous mode
    with sync_playwright() as p:

        # Launch Chromium browser (headless=False to visually see execution)
        browser = p.chromium.launch(headless=False)

        # Create a new browser context with maximized viewport
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080}
        )

        # Open a new page (tab)
        page = context.new_page()

        try:
            # ----------------------------
            # 1. Launch the Application
            # ----------------------------

            # Navigate to the application URL with timeout
            page.goto(URL, timeout=60000)

            # Explicitly wait for username field to be visible
            page.wait_for_selector("input[name='username']", timeout=20000)

            # ----------------------------
            # 2. Automate Login
            # ----------------------------

            # Enter username
            page.fill("input[name='username']", USERNAME)

            # Enter password
            page.fill("input[name='password']", PASSWORD)

            # Click on Login button
            page.click("button[type='submit']")

            # Wait for Dashboard breadcrumb to confirm successful login
            page.wait_for_selector(
                "span.oxd-topbar-header-breadcrumb", timeout=20000
            )

            # Assertion: Verify Dashboard label text
            dashboard_label = page.locator(
                "span.oxd-topbar-header-breadcrumb"
            )
            assert dashboard_label.inner_text() == "Dashboard", \
                "Login failed: Dashboard label not visible"

            print("Login successful")

            # ----------------------------
            # 3. Perform Action 1:
            # Navigate to PIM → Add Employee
            # ----------------------------

            # Click on PIM menu
            page.click("a:has-text('PIM')")

            # Wait for Add button to be visible
            page.wait_for_selector("button:has-text('Add')", timeout=20000)

            # Click on Add Employee button
            page.click("button:has-text('Add')")

            # Wait for Add Employee page heading
            page.wait_for_selector(
                "h6:has-text('Add Employee')", timeout=20000
            )

            # Assertion: Verify Add Employee page is visible
            assert page.locator(
                "h6:has-text('Add Employee')"
            ).is_visible(), "Add Employee page not visible"

            # Enter employee first and last name
            page.fill("input[name='firstName']", "John")
            page.fill("input[name='lastName']", "Doe")

            print("Add Employee page verified")

            # ----------------------------
            # 4. Perform Action 2:
            # Navigate to My Info section
            # ----------------------------

            # Click on My Info tab
            page.click("a:has-text('My Info')")

            # Wait for Personal Details heading
            page.wait_for_selector(
                "h6:has-text('Personal Details')", timeout=20000
            )

            # Assertion: Verify Personal Details section is visible
            assert page.locator(
                "h6:has-text('Personal Details')"
            ).is_visible(), "My Info page not loaded"

            print("My Info page verified")

        # ----------------------------
        # Exception Handling
        # ----------------------------

        # Handle timeout-related issues
        except TimeoutError as e:
            page.screenshot(path="timeout_error.png")
            print("Timeout occurred:", e)

        # Handle assertion failures
        except AssertionError as e:
            page.screenshot(path="assertion_error.png")
            print("Assertion failed:", e)

        # ----------------------------
        # Cleanup
        # ----------------------------

        finally:
            # Close browser context and browser
            context.close()
            browser.close()


# Entry point for script execution
if __name__ == "__main__":
    test_orangehrm()