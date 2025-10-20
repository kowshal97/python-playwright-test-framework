from playwright.sync_api import sync_playwright

text_alert = []

def handle_dialog(dialog):
    message = dialog.message
    text_alert.append(message)
    dialog.accept(prompt_text='leodas')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Alerts.html")

    # Click "Alert with OK & Cancel" tab
    page.locator("//a[@href='#CancelTab']").click()
    page.wait_for_timeout(1000)

    # Attach the dialog handler
    page.on("dialog", handle_dialog)

    # Click the button that triggers the alert
    page.locator("//div[@id='CancelTab']/button").click()
    page.wait_for_timeout(1000)

    # Print captured alert message
    print("Captured Alert Message:", text_alert[0])

    browser.close()

    # to control alert by pressing accept or dismiss
    # page.on("dialog",lambda dialog: dialog.dismiss())
    # page.on("dialog", lambda dialog: dialog.accept())
