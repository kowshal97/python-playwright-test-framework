import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope='module')
def browser_handle():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--window-position=0,0", "--window-size=2560,1440"])
        yield browser
        browser.close()

@pytest.fixture(scope='function')
def page_handle(browser_handle):
    context = browser_handle.new_context(viewport=None)
    page = context.new_page()
    page.set_default_timeout(10_000)
    page.set_default_navigation_timeout(30_000)
    yield page
    page.close()
    context.close()

@pytest.fixture
def home_page(page_handle):
    page = page_handle
    page.goto("http://automationexercise.com",wait_until="domcontentloaded")
    assert page.url.rstrip('/') == "https://automationexercise.com", f"{page.url}is not a homepage"
    page.wait_for_selector("a[href='/'] img",state="visible",timeout=5000)
    print("homepage verified")
    return page

@pytest.fixture
def login_page(home_page):
    page = home_page
    page.wait_for_selector("a[href='/login']", state="visible", timeout=5000).click()
    login_text = page.wait_for_selector("//h2[normalize-space()='Login to your account']", state="visible",timeout=5000).text_content()
    assert login_text == "Login to your account", f"{login_text} is not visible"
    print("login page verified")
    return page

@pytest.fixture
def signup_page(login_page):
    page = login_page
    signup_text = page.wait_for_selector("//h2[normalize-space()='New User Signup!']").text_content()
    assert signup_text == "New User Signup!", f"{signup_text} is not visible"
    print("signup page verified")
    return page

@pytest.fixture
def all_product_page(page_handle):
    page = page_handle
    page.goto("http://automationexercise.com",wait_until="domcontentloaded")
    page.locator("//a[@href='/products']").click()
    current_url = page.url
    assert current_url == "https://automationexercise.com/products",f"{current_url} is not the expected url"
    print("user on right page")
    return page