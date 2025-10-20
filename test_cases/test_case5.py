import pytest
from playwright.sync_api import sync_playwright

def test_verify_user_with_existing_email(signup_page):
    page = signup_page
    name = page.wait_for_selector("//input[@placeholder='Name']")
    name.fill("riley")
    email = page.wait_for_selector("//input[@data-qa='signup-email']")
    email.fill("riley@gmail.com")
    signup_button = page.wait_for_selector("//button[normalize-space()='Signup']")
    signup_button.click()
    page.wait_for_timeout(2000)

    text = page.wait_for_selector("//p[normalize-space()='Email Address already exist!']").text_content()
    assert text == "Email Address already exist!",f"{text} is not the expected text"
    print("Email Address already exist! text verified")