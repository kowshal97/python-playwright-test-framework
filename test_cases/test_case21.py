import pytest

def test_Add_to_cart_from_Recommended_items(page_handle):
    page = page_handle
    page.goto("https://automationexercise.com/")
    recommended_items = page.wait_for_selector("//h2[normalize-space()='recommended items']",state="visible")
    recommended_items.scroll_into_view_if_needed()
    text = recommended_items.text_content().strip()
    assert text == "recommended items",f"{text} is not the expected text"
    print(f"Recommended Items: {text} is visible")

    recommended_product = page.locator("//div[@class='item active']//div[2]//div[1]//div[1]//div[1]")
    product_name = recommended_product.locator("p").text_content().strip()
    print(f"Recommended product name: {product_name}")
    recommended_product.locator("a").click()
    page.wait_for_selector("//u[normalize-space()='View Cart']", state="visible", timeout=10000).click()

    # Verify product in cart
    cart_product = page.wait_for_selector("//td[@class='cart_description']").text_content().strip()
    assert product_name in cart_product, f"Expected '{product_name}' in cart, but got '{cart_product}'"
    print(f"Product: {cart_product} is visible")


