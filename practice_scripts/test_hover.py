from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")

    switch = page.wait_for_selector('//a[@href="SwitchTo.html"]')
    switch.hover()
    switch.click()
    page.wait_for_timeout(2000)
    windows = page.wait_for_selector("//a[@href='Windows.html']")
    windows.hover()
    windows.click()
    page.wait_for_timeout(2000)

    #if yu want doubleclikc
    #switch.dblclick()

    #if yu want right click
    #switch.click(button="right")

    #if yuu want to shift +click
    #switch.click(modifiers=["shift"])

    #if yu want keyboard action
    #switch.press('A')