from playwright.sync_api import sync_playwright

#synnax = page.select_option("xpath",label = "text")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Index.html")
    email = page.wait_for_selector("#email")
    email.type("test@gmail.com")
    button = page.wait_for_selector("#enterimg")
    button.click()


    page.select_option('//select[@id="Skills"]',label='Data Analytics')
    page.wait_for_timeout(3000)
    browser.close()