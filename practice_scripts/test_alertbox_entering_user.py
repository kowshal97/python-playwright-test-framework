from playwright.sync_api import sync_playwright
from test_alert_dialogbox import handle_dialog,text_alert


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Alerts.html")
    page.locator("//a[@href='#Textbox']").click()
    page.wait_for_timeout(2000)
    page.on("dialog", handle_dialog)
    page.wait_for_timeout(2000)
    page.locator("//div[@id='Textbox']//button").click()
    page.wait_for_timeout(2000)