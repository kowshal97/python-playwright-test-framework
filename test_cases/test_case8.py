import pytest

def test_verify_product_detail_page(home_page):
    page = home_page
    product = page.wait_for_selector("//a[@href='/products']",state="visible",timeout=10000)
    print("product",product.is_visible())
    product.click()
    products_url = page.url
    assert products_url == "https://automationexercise.com/products",f"{products_url} is not the expected url"
    print("user is navigated to products page successfully")

    product_list = page.wait_for_selector("//img[@src='/get_product_picture/2']",state="visible",timeout=10000)
    print("product_list1",product_list.is_visible())
    page.wait_for_selector("//div[@class='col-sm-9 padding-right']//div[2]//div[1]//div[2]//ul[1]//li[1]//a[1]").click()

    details_page = page.url
    assert details_page == "https://automationexercise.com/product_details/1",f"{details_page} is not the expected url"
    print("User is landed to product detail page")

    product_information = page.query_selector_all("//div[@class='product-information']")
    for i in product_information:
        print(i.is_visible())
        print(i.text_content().strip())
    print("Product details is visible")