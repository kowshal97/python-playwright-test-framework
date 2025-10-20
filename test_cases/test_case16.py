import pytest

def test_Remove_Products_From_cart(home_page):
    page = home_page
    product = page.locator("//img[@src='/get_product_picture/38']")
    product.scroll_into_view_if_needed()
    product.hover()
    page.wait_for_timeout(1000)
    page.wait_for_selector("(//a[@class='btn btn-default add-to-cart'][normalize-space()='Add to cart'])[58]",state="visible",timeout=10000).click()
    page.wait_for_selector("//u[normalize-space()='View Cart']",state="visible",timeout=10000).click()
    current_url = page.url
    assert current_url == "https://automationexercise.com/view_cart",f"{current_url} is not the expected url"
    print("User in correct page")

    product = page.wait_for_selector("//a[normalize-space()='Rose Pink Embroidered Maxi Dress']",state="visible",timeout=10000)
    product_name = product.text_content().strip()
    print(f"Product name: {product_name}")

    page.wait_for_selector("//td[@class='cart_delete']", state="visible", timeout=10000).click()

    page.wait_for_selector("//tr[@id='product-38']", state="detached", timeout=10000)
    print("Product successfully removed from cart")

