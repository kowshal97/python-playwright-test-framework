import pytest

def test_View_Category_Products(page_handle):
    page = page_handle
    page.goto("https://automationexercise.com")
    category = page.wait_for_selector("//h2[normalize-space()='Category']")
    assert category.is_visible(),f"{category} is not visible"
    print(f"category is visible: {category}")
    women_category = page.wait_for_selector("//a[normalize-space()='Women']",state="visible",timeout=10000)
    women_category.click()
    dress = page.wait_for_selector("//div[@id='Women']//a[contains(text(),'Dress')]")
    dress.click()

    category_page = page.url
    if category_page == "https://automationexercise.com/category_products/1":
        print("user in correct page")
        category_title = page.wait_for_selector("//h2[normalize-space()='Women - Dress Products']").text_content().strip()
        assert category_title == "Women - Dress Products",f"{category_title} is not the expected title"
        print(f"category title is visible: {category_title}")

    men_category = page.wait_for_selector("//a[normalize-space()='Men']",state="visible",timeout=10000)
    men_category.click()
    tshirt = page.wait_for_selector("//a[normalize-space()='Tshirts']")
    tshirt.click()
    men_category_page = page.url
    assert men_category_page == "https://automationexercise.com/category_products/3",f"{men_category_page} is not the expected url"
    print(f"user in correct page: {men_category_page}")

