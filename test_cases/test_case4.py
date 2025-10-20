import pytest
from playwright.sync_api import sync_playwright

def test_logout_user(login_page):
        page = login_page
        email = page.wait_for_selector("input[data-qa='login-email']", state="visible", timeout=5000)
        email.fill("riley@gmail.com")
        password = page.wait_for_selector("input[placeholder='Password']", state="visible", timeout=5000)
        password.fill("riley123")
        page.wait_for_timeout(5000)
        login_button = page.wait_for_selector("button[data-qa='login-button']", state="visible", timeout=5000)
        login_button.click()

        log_out = page.wait_for_selector("//a[normalize-space()='Logout']").click()
        current = page.url
        assert current == "https://automationexercise.com/login",f"{current} is not the expected url"



