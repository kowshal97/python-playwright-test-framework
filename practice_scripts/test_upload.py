from playwright.sync_api import sync_playwright
from pathlib import Path

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.automationtesting.in/FileUpload.html")
    page.wait_for_timeout(2000)

    upload_location = page.wait_for_selector("//*[@id='input-4']")
    file_upload = Path(r"C:\Users\Kowzs\Desktop\Resume\Non IT fields\Kowshal_Sugunarajah_Resume.pdf")

    upload_location.set_input_files(file_upload)
    page.wait_for_timeout(2000)