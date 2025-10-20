import pytest
from uuid import uuid4

def test_Place_Order_Register_while_Checkout(home_page):
    page = home_page


    product1 = page.wait_for_selector("//img[@src='/get_product_picture/1']")
    product1.hover()
    page.wait_for_selector("//a[@data-product-id='1']", state="visible", timeout=10000).click()
    page.wait_for_timeout(1000)
    page.wait_for_selector("//button[normalize-space()='Continue Shopping']",state="visible",timeout=10000).click()


    page.wait_for_selector("//a[normalize-space()='Cart']").click()
    current_url = page.url
    assert current_url == "https://automationexercise.com/view_cart", f"{current_url} is not the expected url"
    print("User is on the cart page")


    page.wait_for_selector("//a[normalize-space()='Proceed To Checkout']", state="visible", timeout=10000).click()
    page.wait_for_selector("//u[normalize-space()='Register / Login']", state="visible", timeout=10000).click()


    name = page.wait_for_selector("//input[@placeholder='Name']")
    name.fill("raja")
    email = page.wait_for_selector("//input[@data-qa='signup-email']")
    unique_email = f"raja_{uuid4().hex[:8]}@gmail.com"
    email.fill(unique_email)
    page.wait_for_selector("//button[normalize-space()='Signup']").click()


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


    account_created = page.wait_for_selector("//b[normalize-space()='Account Created!']").text_content().strip()
    assert account_created == "Account Created!", f"{account_created} is not visible"
    page.wait_for_selector("//a[normalize-space()='Continue']").click()


    page.wait_for_selector("//a[normalize-space()='Cart']//i[@class='fa fa-shopping-cart']", state="visible", timeout=5000).click()
    page.wait_for_selector("//a[normalize-space()='Proceed To Checkout']", state="visible", timeout=10000).click()


    address_items = page.query_selector_all("//ul[@id='address_delivery']/li")
    assert len(address_items) > 0, "No details found in delivery address block"
    print("Address details verified")


    cart_item = page.wait_for_selector("//p[normalize-space()='Women > Tops']")
    cart_item_text = cart_item.text_content().strip()
    assert cart_item_text == "Women > Tops", f"{cart_item_text} is not visible"
    print("Product is verified")


    page.wait_for_selector("//textarea[@name='message']").fill("Product is good")
    page.wait_for_selector("//a[normalize-space()='Place Order']").click()


    page.wait_for_selector("//input[@name='name_on_card']").fill("kowshik")
    page.wait_for_selector("//input[@name='card_number']").fill("123456789")
    page.wait_for_selector("//input[@placeholder='ex. 311']").fill("123")
    page.wait_for_selector("//input[@placeholder='MM']").fill("12")
    page.wait_for_selector("//input[@placeholder='YYYY']").fill("2030")
    page.wait_for_selector("//button[@id='submit']").click()

    # success_message = page.locator("//div[@id='success_message']")
    # success_message.wait_for(state="visible",timeout=10000)
    # text = success_message.text_content().strip()
    # print("found text:", text)
    # assert "Your order has been placed successfully!" in text, f"{text} is not visible"
    # print("Order placed successfully")

    # Delete account
    page.wait_for_selector("//a[normalize-space()='Delete Account']").click()
    deleted = page.wait_for_selector("//b[normalize-space()='Account Deleted!']").text_content().strip()
    assert deleted == "Account Deleted!", f"{deleted} is not visible"
    print("Verified account deleted")
    page.wait_for_selector("//a[normalize-space()='Continue']").click()