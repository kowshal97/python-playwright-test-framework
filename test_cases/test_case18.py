import pytest

def test_View_Cart_Brand_Products(page_handle):
    page = page_handle
    page.goto("http://automationexercise.com")
    page.wait_for_selector("//a[@href='/products']").click()

    brands = page.query_selector_all("//div[@class='brands-name']")
    assert len(brands) > 0, f"{len(brands)} brands were not found"

    for brand in brands:
        brand_name_text = brand.text_content().strip()
        print(f"brand name: {brand_name_text}")
        print("brand name verified")

    page.wait_for_selector("//a[@href='/brand_products/Kookie Kids']").click()
    kookieki_page = page.url
    if kookieki_page == "https://automationexercise.com/brand_products/Kookie%20Kids":
        print("user in correct page")
        title = page.wait_for_selector("//h2[normalize-space()='Brand - Kookie Kids Products']").text_content().strip()
        assert title == title,f"{title} is not the expected title"
        product1 = page.wait_for_selector("//div[@class='productinfo text-center']//p[contains(text(),'Full Sleeves Top Cherry - Pink')]").text_content().strip()
        if product1 == "Full Sleeves Top Cherry - Pink":
            print(f"{product1} was the expected product")
            print("products are visible")

    page.wait_for_selector("//a[@href='/brand_products/Allen Solly Junior']").click()
    new_page = page.url
    assert new_page == "https://automationexercise.com/brand_products/Allen%20Solly%20Junior",f"{new_page} is not the expected url"
    print("user in correct page")

    element = page.wait_for_selector("//div[@class='productinfo text-center']//p[contains(text(),'Sleeveless Unicorn Patch Gown - Pink')]").text_content().strip()
    assert element == "Sleeveless Unicorn Patch Gown - Pink",f"{element} is not the expected text"
    print(f"element name: {element}")
    print("products are visible")