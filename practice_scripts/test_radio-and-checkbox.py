from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Index.html")
    email = page.wait_for_selector("#email")
    email.type("test@gmail.com")
    button = page.wait_for_selector("#enterimg")
    button.click()

    radio = page.wait_for_selector("//input[@value='Male']")
    radio.click()
    if radio.is_checked:
        print("Radio selected")
    else:
        print("Radio not selected")


    checkbox = page.wait_for_selector("//input[@value='Cricket']")
    checkbox.click()
    if checkbox.is_checked:
        print("Checkbox selected")
    else:
        print("Checkbox not selected")


    page.wait_for_timeout(3000)
    browser.close()