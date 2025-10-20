from playwright.sync_api import Page,expect
import re



def test_verifyGoogleTitle(page: Page):
    page.goto("https://www.google.com/")
    expect(page).to_have_title(re.compile("Google"))