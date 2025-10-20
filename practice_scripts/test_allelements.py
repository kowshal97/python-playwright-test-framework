from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    try:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demo.automationtesting.in/Selectable.html")
        page.wait_for_timeout(2000)


        #to find all text in b tag
        elements = page.query_selector_all("b")
        print(len(elements))

        for i in elements:
            print(i.text_content())

        #to find all links in a tag
        links = page.query_selector_all("a")
        print(len(links))
        for i in links:
            print(i.get_attribute("href"))

    except Exception as e:
        print(str(e))
    finally:
        print("execute")
        browser.close()
