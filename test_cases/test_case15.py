from asyncio import timeout

import pytest
from uuid import uuid4

def test_Register_before_Checkout(home_page):
    page = home_page
    page.wait_for_selector("//a[normalize-space()='Signup / Login']").click()

    #to fill details and create account
    name = page.wait_for_selector("//input[@placeholder='Name']")
    name.fill("raja")
    email = page.wait_for_selector("//input[@data-qa='signup-email']")
    unique_email = f"raja_{uuid4().hex[:8]}@gmail.com"
    email.fill(unique_email)
    page.wait_for_selector("//button[normalize-space()='Signup']").click()

    #to fill details
    page.wait_for_selector("//input[@id='id_gender1']").click()
    page.wait_for_selector("//input[@id='password']").fill("123456789")
    page.wait_for_timeout(500)
    page.select_option("//select[@id='days']", label="19")
    page.select_option("//select[@id='months']", label="November")
    page.select_option("//select[@id='years']", label="1997")
    page.wait_for_selector("//input[@id='newsletter']").click()
    page.wait_for_selector("//input[@id='optin']").click()
    page.wait_for_timeout(500)

    page.wait_for_selector("//input[@id='first_name']").fill("Kowshik")
    page.wait_for_selector("//input[@id='last_name']").fill("dhana")
    page.wait_for_selector("//input[@id='company']").fill("Amazon")
    page.wait_for_selector("//input[@id='address1']").fill("florentine place, pickering")
    page.select_option("//select[@id='country']", label="Canada")
    page.wait_for_selector("//input[@id='state']").fill("Ontario")
    page.wait_for_selector("//input[@id='city']").fill("Toronto")
    page.wait_for_selector("//input[@id='zipcode']").fill("0123456")
    page.wait_for_selector("//input[@id='mobile_number']").fill("241947198241")
    page.wait_for_selector("//button[normalize-space()='Create Account']").click()
    page.wait_for_timeout(1000)

    #to verify account text
    account_created = page.wait_for_selector("//b[normalize-space()='Account Created!']").text_content().strip()
    assert account_created == "Account Created!", f"{account_created} is not visible"
    page.wait_for_selector("//a[normalize-space()='Continue']").click()

    #adding product
    product1 = page.wait_for_selector("//img[@src='/get_product_picture/7']")
    product1.scroll_into_view_if_needed()
    product1.hover()
    page.wait_for_selector("//p[normalize-space()='Madame Top For Women']/following::a[contains(@class,'add-to-cart')][1]",state="visible",timeout=5000).click()
    page.wait_for_selector("//u[normalize-space()='View Cart']",state="visible",timeout=10000).click()

    #to verify cart page
    current_url = page.url
    assert current_url == "https://automationexercise.com/view_cart", f"{current_url} is not the expected url"
    print("User is on the cart page")

    # Proceed to checkout
    page.wait_for_selector("//a[normalize-space()='Proceed To Checkout']", state="visible", timeout=10000).click()
    address_items = page.query_selector_all("//ul[@id='address_delivery']")
    for item in address_items:
        address_text = item.text_content().strip()
        print(f"Address detail: {address_text}")
        assert address_text, "Address detail not found or is empty in cart page"
        print("address detail found")

    page.wait_for_selector("//textarea[@name='message']").fill("Product is good")
    page.wait_for_selector("//a[normalize-space()='Place Order']").click()

    #tp place order

    page.wait_for_selector("//input[@name='name_on_card']").fill("kowshik")
    page.wait_for_selector("//input[@name='card_number']").fill("123456789")
    page.wait_for_selector("//input[@placeholder='ex. 311']").fill("123")
    page.wait_for_selector("//input[@placeholder='MM']").fill("12")
    page.wait_for_selector("//input[@placeholder='YYYY']").fill("2030")
    page.wait_for_selector("//button[@id='submit']").click()
    page.screenshot(path="./Screenshots/success_message.png")
    page.wait_for_timeout(2000)


    # #to verify success text
    # success = page.locator("//div[@id='success-subscribe']")
    # success.wait_for(state="visible",timeout=10000)
    # assert success.is_visible(), "Success message is not visible"
    # text = success.text_content().strip()
    # print(f"found text: {text}")
    # assert text == "Your order has been placed successfully!", f"{text} is not visible"
    # print(f"text",{text})

    #to verify account delete
    page.wait_for_selector("//a[normalize-space()='Delete Account']").click()
    deleted = page.wait_for_selector("//b[normalize-space()='Account Deleted!']").text_content().strip()
    assert deleted == "Account Deleted!", f"{deleted} is not visible"
    print("Verified account deleted")
    page.wait_for_selector("//a[normalize-space()='Continue']").click()


