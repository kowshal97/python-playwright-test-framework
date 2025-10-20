import pytest

def test_search_product(home_page):
    page = home_page
    page.wait_for_selector("//a[@href='/products']",state="visible",timeout=10000).click()
    products_url = page.url
    assert products_url == "https://automationexercise.com/products", f"{products_url} is not the expected url"
    print("user is navigated to products page successfully")

    search_button = page.wait_for_selector("//input[@id='search_product']",state="visible",timeout=10000)
    search_button.fill("Tshirts")
    page.wait_for_selector("//i[@class='fa fa-search']").click()

    result = page.wait_for_selector("//h2[normalize-space()='Searched Products']").text_content().strip()
    assert result == "Searched Products",f"{result} is not visible"
    print("Searched Products is visible")

    all_search_products = page.query_selector_all("//div[@class='productinfo text-center']")
    assert all_search_products, "No products found in search results"

    keywords = ["tshirt", "t-shirt", "t shirt"]
    for i, product in enumerate(all_search_products, start=1):
        product_name_element = product.query_selector("p")
        assert product_name_element is not None, f"Product {i} has no name element"
        product_name = product_name_element.text_content().strip().lower()
        print(f"Product {i}: {product_name}")
        assert any(keyword in product_name for keyword in keywords), \
            f"Product '{product_name}' does not match expected tshirt keywords"
    print("all the products related to search are visible")