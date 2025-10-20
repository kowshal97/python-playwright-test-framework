import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.usefixtures('browser_handle')
class Test_login_user_with_incorrect_credentials:
    def test_verify_homepage(self,home_page):
        print("homepage is visible")


    def test_verify_login_text(self,login_page):
        print("Login to your account is visible")

    def test_login_with_Invalid_credentials(self,login_page):
        page = login_page
        email = page.wait_for_selector("input[data-qa='login-email']", state="visible", timeout=5000)
        email.fill("leo1@gmail.com")
        password = page.wait_for_selector("input[placeholder='Password']", state="visible", timeout=5000)
        password.fill("leo1")
        page.wait_for_timeout(5000)
        login_button = page.wait_for_selector("button[data-qa='login-button']", state="visible", timeout=5000)
        login_button.click()

        error_text = page.wait_for_selector("//p[normalize-space()='Your email or password is incorrect!']", state="visible",timeout=5000).text_content()
        assert "Your email or password is incorrect!" in error_text,f"{error_text}is not visible"