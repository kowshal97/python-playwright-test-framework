import pytest

def test_Verify_Subscription_in_Cart_page(home_page):
    page = home_page
    cart = page.wait_for_selector("//body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]").click()
    subscription = page.wait_for_selector("//h2[normalize-space()='Subscription']", state="visible", timeout=10000)
    subscription.scroll_into_view_if_needed()
    subscription_text = subscription.text_content().strip()
    assert subscription_text == "Subscription", f"{subscription_text}" is not visible
    print("subscription text is visible")
    page.wait_for_timeout(2000)

    page.wait_for_selector("//input[@id='susbscribe_email']").fill("leo@gmail.com")
    page.wait_for_selector("//button[@id='subscribe']").click()

    success_locator = page.locator("//div[@class='alert-success alert']")
    success_locator.wait_for(state="visible", timeout=10000)
    message_text = success_locator.text_content().strip()
    print("Found text:", message_text)
    page.screenshot(path="./Screenshots/subscription_message11.png")
    assert message_text == "You have been successfully subscribed!", f"{message_text} is not visible"
    print("Success message text is visible")


