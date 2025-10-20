import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.usefixtures('browser_handle')
class Test_login_user:
    def test_verify_homepage(self,home_page):
        print("homepage is visible")


    def test_verify_login(self,page_handle):
        page = page_handle
        page.goto("https://automationexercise.com")
        page.wait_for_selector("a[href='/login']",state="visible",timeout=5000).click()
        login_text = page.wait_for_selector("//h2[normalize-space()='Login to your account']",state="visible",timeout=5000).text_content()
        assert login_text == "Login to your account",f"{login_text} is not visible"


    def test_login_with_valid_credentials(self,page_handle):
        page = page_handle
        page.goto("https://automationexercise.com")
        page.wait_for_selector("a[href='/login']", state="visible", timeout=5000).click()
        email = page.wait_for_selector("input[data-qa='login-email']", state="visible", timeout=5000)
        email.fill("india@gmail.com")
        password = page.wait_for_selector("input[placeholder='Password']", state="visible", timeout=5000)
        password.fill("india")
        login_button = page.wait_for_selector("button[data-qa='login-button']", state="visible", timeout=5000)
        login_button.click()
        delete_account = page.wait_for_selector("a[href='/delete_account']", state="visible", timeout=5000)
        delete_account.click()

        delete_text = page.wait_for_selector("//b[normalize-space()='Account Deleted!']",state="visible", timeout=5000).text_content()
        assert delete_text == "Account Deleted!",f"{delete_text} is not visible"


