from playwright.sync_api import sync_playwright

def handle_rejex(response):
    if "https://www.plus2net.com/php_tutorial/dd-ajax.php?" in response.url:
        status = response.status
        data = response.text()
        print(f"status:{status},data: {data}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.plus2net.com/php_tutorial/ajax_drop_down_list-demo.php")
    page.wait_for_timeout(2000)

    #to select the text or value by code
    # category = page.wait_for_selector("//*[@id='s1']")
    # category.select_option(label='Fruits')
    #
    # sub_category = page.wait_for_selector("//*[@id='s2']")
    # sub_category.select_option(label='Apple')

    #to check the ajax links if yu click the link it should give the response
    category = page.wait_for_selector("//*[@id='s1']")
    page.on("response", lambda response: handle_rejex(response))
    category.select_option('4')
    page.wait_for_timeout(2000)
