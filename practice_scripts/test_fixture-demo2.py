import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="class")
def chromium_browser(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        request.cls.browser = browser
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(chromium_browser):
    context = chromium_browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.mark.usefixtures("chromium_browser")
class TestTitleClass:
    def test_google(self, page):
        page.goto("https://www.google.com", wait_until="domcontentloaded")
        assert "Google" in page.title()  # use method and loose match

    def test_youtube(self, page):
        page.goto("https://www.youtube.com", wait_until="domcontentloaded")
        assert "YouTube" in page.title()  # titles vary; avoid exact match

    def test_amazon(self, page):
        page.goto("https://www.amazon.com", wait_until="domcontentloaded")
        assert "Amazon" in page.title()   # region-specific titles vary

    @pytest.mark.parametrize("invalid_username, invalid_password", [("admin", "asdad"), ("asdad", "afasfaf"), ])
    def test_login(self,page, invalid_username, invalid_password):
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.wait_for_selector("//input[@name='username']").type(invalid_username)
        page.wait_for_selector("//input[@name='password']").type(invalid_password)
        page.wait_for_timeout(3000)
        page.wait_for_selector("//button[@type='submit']").click()
        error_message = page.wait_for_selector("//div[@role='alert']//p").text_content()
        assert error_message == 'Invalid credentials'


