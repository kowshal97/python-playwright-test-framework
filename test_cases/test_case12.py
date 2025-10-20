from statistics import quantiles

import pytest

def test_verfiy_add_to_cart(home_page):
    page = home_page
    page.wait_for_selector("//a[@href='/products']",state="visible",timeout=10000).click()
    page.wait_for_timeout(2000)

    first_product = page.wait_for_selector("//img[@src='/get_product_picture/1']")
    first_product.scroll_into_view_if_needed()
    first_product.hover()
    page.wait_for_timeout(5000)
    add_to_cart = page.wait_for_selector("//a[@data-product-id='1']",state="visible",timeout=10000)
    add_to_cart.click()
    page.wait_for_selector("//button[normalize-space()='Continue Shopping']",state="visible",timeout=10000).click()

    second_product = page.wait_for_selector("//img[@src='/get_product_picture/2']")
    second_product.scroll_into_view_if_needed()
    second_product.hover()
    page.wait_for_timeout(5000)
    add_to_cart2 = page.wait_for_selector("//a[@data-product-id='2']",state="visible",timeout=10000)
    add_to_cart2.click()

    view_cart = page.wait_for_selector("//u[normalize-space()='View Cart']").click()

    cart_product1 = page.query_selector_all("//tr[@id='product-1']")
    assert cart_product1, "No products found in cart page"


    for i, product in enumerate(cart_product1, start=1):
        product_name = product.query_selector("p")
        name = page.wait_for_selector("//tr[@id='product-1']//td[@class='cart_description']").text_content().strip()
        quantity = page.wait_for_selector("//tr[@id='product-1']//td[@class='cart_quantity']").text_content().strip()
        price = page.wait_for_selector("//tr[@id='product-1']//td[@class='cart_price']").text_content().strip()
        total_price = page.wait_for_selector("//tr[@id='product-1']//td[@class='cart_total']").text_content().strip()

        print(f"item: {i}")
        print(f"name: {name}")
        print(f"quantity: {quantity}")
        print(f"price: {price}")
        print(f"total_price: {total_price}")
        print("details verified")

    cart_product2 = page.query_selector_all("//tr[@id='product-2']")
    assert cart_product2, "No products found in cart page"

    for i, product1 in enumerate(cart_product1, start=1):
        product_name = product1.query_selector("p")
        name = page.wait_for_selector("//p[normalize-space()='Men > Tshirts']").text_content().strip()
        quantity = page.wait_for_selector(
            "//tr[@id='product-2']//td[@class='cart_quantity']").text_content().strip()
        price = page.wait_for_selector("//tr[@id='product-2']//td[@class='cart_price']").text_content().strip()
        total_price = page.wait_for_selector(
            "//tr[@id='product-2']//td[@class='cart_total']").text_content().strip()

        print(f"item: {i}")
        print(f"name: {name}")
        print(f"quantity: {quantity}")
        print(f"price: {price}")
        print(f"total_price: {total_price}")
        print("details verified")








