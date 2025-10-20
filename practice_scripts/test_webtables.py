from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=200)
    context = browser.new_context()
    page = context.new_page()


    page.goto("https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html",
              wait_until="domcontentloaded", timeout=45000)


    table = page.wait_for_selector("table#customers", state="visible", timeout=20000)


    tr = table.query_selector_all("tr")
    print(len(tr))

    # for row in tr:
    #     print(row.text_content().strip())

    td = table.query_selector_all("td")
    print(len(td))

    for row in tr:
        cells = row.query_selector_all("td")
        for cell in cells:
            print(cell.text_content().strip())


    browser.close()
