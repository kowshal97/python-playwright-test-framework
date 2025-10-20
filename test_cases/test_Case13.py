import pytest

def test_Verify_Product_quantity_in_Cart(home_page):
    page = home_page
    page.wait_for_selector("//a[@href='/products']",state="visible",timeout=10000).click()
    page.wait_for_selector("//div[@class='col-sm-9 padding-right']//div[2]//div[1]//div[2]//ul[1]//li[1]//a[1]").click()

    product_detail = page.query_selector_all("//div[@class='product-information']")
    assert product_detail,"No detail found in cart page"

    for product in product_detail:
        product_detail_name = product.text_content().strip()
        print(f"product_detail_name: {product_detail_name}")
        assert product_detail_name, "No product detail found in cart page"

    quantity = page.wait_for_selector("//input[@id='quantity']",state="visible",timeout=10000)
    quantity.fill("4")
    page.wait_for_selector("//button[normalize-space()='Add to cart']",state="visible",timeout=10000).click()
    page.wait_for_timeout(2000)
    page.wait_for_selector("//u[normalize-space()='View Cart']",state="visible",timeout=10000).click()

    quantity_number = page.wait_for_selector("//button[normalize-space()='4']").text_content().strip()
    assert int(quantity_number) == 4,f"Correct quantity not found in cart page"
    print(f"Correct quantity: {quantity_number}")
    print("Quantity verified")