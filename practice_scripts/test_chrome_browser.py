import pytest
from playwright.sync_api import sync_playwright
from test_fixture_demo import page,browser

def test_login(page):
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("https://google.com")
    assert page.title() == "Google"
    page.wait_for_timeout(1000)
