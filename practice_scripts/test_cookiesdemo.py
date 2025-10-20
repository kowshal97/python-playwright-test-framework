
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.redbus.in/")

    #to check cookies
    my_cookies = page.context.cookies()
    print(my_cookies)

    #to clear cookies
    page.context.clear_cookies()

    #to add new cookies
    new_cookies = {
        'name' : 'leo',
        'value': 'leodas123',
        "url": "https://www.redbus.in"
    }
    page.context.add_cookies([new_cookies])

    #to take screenshot
    page.screenshot(path='test.png',full_page=True)
