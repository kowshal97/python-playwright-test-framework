import pytest
from playwright.sync_api import expect


def test_Add_review_on_product(all_product_page):
    page = all_product_page
    page.wait_for_selector("//a[@href='/product_details/1']").click()

    #o verify write your review
    review = page.wait_for_selector("//a[normalize-space()='Write Your Review']",state="visible",timeout=10000).text_content().strip()
    assert review == "Write Your Review",f"{review} is not the expected text"
    print("review is visible")

    #to fill revieww
    page.fill("//input[@id='name']",'kowshal')
    page.fill("//input[@id='email']",'kowshal@gmail.com')
    page.fill("//textarea[@id='review']",'This is a bad product')
    page.click("//button[@id='button-review']")

    #to verify text alert
    alert = page.locator("div.alert-success.alert > span")
    expect(alert).to_be_visible(timeout=5000)
    msg = alert.inner_text()
    print("Success banner:", msg)
    expect(alert).to_have_text("Thank you for your review.", timeout=1000)
    expect(alert).to_be_hidden(timeout=5000)
