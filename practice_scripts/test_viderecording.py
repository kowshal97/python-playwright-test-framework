from playwright.sync_api import sync_playwright

from test_xpath import username

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir='./videos')
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_timeout(2000)

    user_name = page.wait_for_selector("//input[@name='username']")
    user_name.type("Admin")
    pass_word = page.wait_for_selector("//input[@name='password']")
    pass_word.type("admin123")
    page.screenshot(path="./screenshot/homepagee.png")
    page.wait_for_timeout(2000)
    page.wait_for_selector('//button[@type="submit"]').click()
    page.wait_for_timeout(2000)
    page.screenshot(path="./screenshot/homepagee1.png")
