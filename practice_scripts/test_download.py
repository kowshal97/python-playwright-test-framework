from playwright.sync_api import sync_playwright

def download_handle(download):
    location_file = "./files/test.zip"
    download.save_as(location_file)



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.goto("https://demo.automationtesting.in/FileDownload.html")
    page.wait_for_timeout(2000)

    text_box = page.wait_for_selector("#textbox")
    text_box.type("This is kowshal")
    generate = page.wait_for_selector("#createTxt")
    generate.click()

    page.on("download",download_handle)
    page.wait_for_selector("#link-to-download").click()
    page.wait_for_timeout(2000)

