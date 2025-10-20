import pytest

def test_verify_testcase_page(home_page):
    page = home_page
    page.wait_for_selector("//div[@class='item active']//button[@type='button'][normalize-space()='Test Cases']", state="visible",timeout=10000).click()
    page.wait_for_timeout(2000)
    testcase_url = page.url
    assert testcase_url == "https://automationexercise.com/test_cases",f"{testcase_url} is not the expected url"
    print("user is navigated to test cases page successfully")