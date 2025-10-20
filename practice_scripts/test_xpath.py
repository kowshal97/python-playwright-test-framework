from playwright.sync_api import Playwright, sync_playwright

#tagname[@attribute="value"]
#to use text = //tagname[text()="text"]
#page.wait_for_selector("//p[text()='Forgot your password? ']").click()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    username = page.wait_for_selector("//input[@name='username']")
    username.type("Admin")
    password = page.wait_for_selector("//input[@name='password']")
    password.type("admin123")
    button = page.wait_for_selector("//button[@type='submit']")
    button.click()
    page.wait_for_timeout(3000)
    browser.close()



