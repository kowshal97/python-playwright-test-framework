import pytest

def test_verify_Scroll_up_without_arrow(home_page):
    page = home_page
    age = home_page
    page.keyboard.press("PageDown")
    page.keyboard.press("End")

    # to verify subscription text
    subscription = page.wait_for_selector("//h2[normalize-space()='Subscription']").text_content().strip()
    assert subscription == "Subscription", text is not visible
    print("Subscription verified:", subscription)
    page.keyboard.press("Home")

    # to verify header text
    header = page.wait_for_selector(
        "//div[@class='item active']//h2[contains(text(),'Full-Fledged practice website for Automation Engin')]",
        state="visible", timeout=10000)
    header_text = header.text_content().strip()
    assert header_text == "Full-Fledged practice website for Automation Engineers", f"header text is not visible: {header_text}"
    print("Full-Fledged practice website for Automation Engin is visible:", header_text)