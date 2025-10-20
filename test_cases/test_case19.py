import pytest

def test_Search_Products_and_Verify_Cart_After_Login(all_product_page):
    page = all_product_page
    page.locator("//input[@id='search_product']").fill("tshirt")
    page.locator("//i[@class='fa fa-search']").click()
    searched_product = page.wait_for_selector("//h2[normalize-space()='Searched Products']",state='visible',timeout=10000).text_content().strip()
    assert searched_product == "Searched Products",f"{searched_product} is not the expected text"

    #to verfiy searched producs are visisble
    all_product = page.query_selector_all("//div[@class='col-sm-9 padding-right']")
    assert all_product ,f"{all_product} has no products"

    for product in all_product:
        p_tags = product.query_selector_all("p")
        for p in p_tags:
            assert p,f"{p.text_content()} should be displayed"
            print("P tag content:", p.text_content().strip())
        print("all products related to search is visible")

    # to add those products in cart
    first_product = page.wait_for_selector("//img[@src='/get_product_picture/29']",state='visible',timeout=10000)
    first_product.scroll_into_view_if_needed()
    first_product.hover()
    page.wait_for_selector("//a[@data-product-id='29']").click()
    page.wait_for_timeout(2000)
    page.wait_for_selector("//button[normalize-space()='Continue Shopping']").click()

    second_product = page.wait_for_selector("//a[@data-product-id='31']", state='visible', timeout=10000)
    second_product.scroll_into_view_if_needed()
    second_product.hover()
    page.wait_for_selector("//a[@data-product-id='31']").click()
    page.wait_for_selector("//u[normalize-space()='View Cart']").click()


    #to verify product in card
    cart_info = page.query_selector_all("//table[@id='cart_info_table']")
    for cart in cart_info:
        product1 = cart.wait_for_selector("//a[normalize-space()='Green Side Placket Detail T-Shirt']").text_content().strip()
        product2 = cart.wait_for_selector("//a[normalize-space()='Pure Cotton Neon Green Tshirt']").text_content().strip()
        assert product1,f"{product1} is not the expected text"
        assert product2,f"{product2} is not the expected text"
        print(product1,product2)
        print("products are visible")
    page.wait_for_selector("//a[normalize-space()='Signup / Login']").click()

    #to login
    page.fill("//input[@data-qa='login-email']","kowshal@gmail.com")
    page.fill("//input[@placeholder='Password']","123456789")
    page.click("//button[normalize-space()='Login']")
    page.click("//a[normalize-space()='Cart']")

    #to verify again
    cart_info1 = page.query_selector_all("//table[@id='cart_info_table']")
    for cart in cart_info1:
        product11 = cart.wait_for_selector(
            "//a[normalize-space()='Green Side Placket Detail T-Shirt']").text_content().strip()
        product22 = cart.wait_for_selector(
            "//a[normalize-space()='Pure Cotton Neon Green Tshirt']").text_content().strip()
        assert product11, f"{product11} is not the expected text"
        assert product22, f"{product22} is not the expected text"
        print(product11, product22)
        print("products are visible")





