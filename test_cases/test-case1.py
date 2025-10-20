import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.usefixtures('browser_handle')
class Test_register_user:
    def test_verify_homepage(self,page_handle):
        page = page_handle
        try:
            page.goto("http://automationexercise.com",wait_until="domcontentloaded")
            if page.url.rstrip('/') != 'https://automationexercise.com':
                pytest.fail(f"{page.url} is not a homepage")

            page.wait_for_selector("//a[@href='/']/img",state ="visible",timeout=5000)
            print("homepage is visible")
        except Exception as e:
            pytest.fail(f"homepage check failed: {e}")

    def test_verify_signup_text(self,page_handle):
        page = page_handle
        try:
            page.goto("http://automationexercise.com")
            login_button = page.wait_for_selector("//a[@href='/login']").click()
            page.wait_for_timeout(2000)
            new_sign_up = page.locator("//h2[text() = 'New User Signup!']").text_content()
            if new_sign_up == "New User Signup!":
                print("New user signup is visible")
            else:
                pytest.fail(f"{new_sign_up} is not visible")
        except Exception as e:
            pytest.fail(f"New user signup check failed: {e}")

    @pytest.mark.parametrize("valid_name, valid_gmail,pass_word",[("rambo",'rambo1@gmail.com','john123')])
    def test_new_user_signup(self,page_handle,valid_name,valid_gmail,pass_word):
        page = page_handle
        try:
            #to fill new sign up form
            page.goto("https://automationexercise.com/login")
            name = page.wait_for_selector("//input[@placeholder='Name']")
            name.fill(valid_name)
            email = page.wait_for_selector("//input[@data-qa='signup-email']")
            email.fill(valid_gmail)
            sign_up_button = page.wait_for_selector("//button[normalize-space()='Signup']").click()
            page.wait_for_timeout(2000)

            #to check the account info text
            account_info = page.locator("//b[normalize-space()='Enter Account Information']").text_content()
            if account_info == "Enter Account Information":
                print("Account info is visible")
            else:
                pytest.fail(f"{account_info} is not visible")
                page.wait_for_timeout(2000)

            #to fill details
            mr = page.wait_for_selector("//input[@id='id_gender1']")
            mr.click()
            password = page.wait_for_selector("//input[@id='password']")
            password.fill(pass_word)
            page.wait_for_timeout(2000)
            page.select_option("//select[@id='days']",label="19")
            page.select_option("//select[@id='months']",label="November")
            page.select_option("//select[@id='years']",label="1997")
            page.wait_for_selector("//input[@id='newsletter']").click()
            page.wait_for_selector("//input[@id='optin']").click()
            page.wait_for_timeout(2000)

            #to fill form details like fullname
            full_name = page.wait_for_selector("//input[@id='first_name']")
            full_name.fill("john")
            last_name = page.wait_for_selector("//input[@id='last_name']")
            last_name.fill("cena")
            company = page.wait_for_selector("//input[@id='company']")
            company.fill("Amazon")
            address = page.wait_for_selector("//input[@id='address1']")
            address.fill("florentine place, pickering")
            page.select_option("//select[@id='country']", label="Canada")
            state = page.wait_for_selector("//input[@id='state']")
            state.fill("Ontario")
            city = page.wait_for_selector("//input[@id='city']")
            city.fill("Toronto")
            zipcode = page.wait_for_selector("//input[@id='zipcode']")
            zipcode.fill("0123456")
            mobile = page.wait_for_selector("//input[@id='mobile_number']")
            mobile.fill("241947198241")
            page.wait_for_selector("//button[normalize-space()='Create Account']").click()
            page.wait_for_timeout(2000)

            #to check account created
            account_created = page.wait_for_selector("//b[normalize-space()='Account Created!']").text_content()
            if account_created == "Account Created!":
                print("Account created is visible")
            else:
                pytest.fail(f"{account_created} is not visible")
            page.wait_for_timeout(2000)

            continue_button = page.wait_for_selector("//a[normalize-space()='Continue']")
            continue_button.click()

            #to delete
            delete_user = page.wait_for_selector("//a[normalize-space()='Delete Account']")
            delete_user.click()
            page.wait_for_timeout(2000)

            #verify account deletion
            deleted = page.wait_for_selector("//b[normalize-space()='Account Deleted!']").text_content()
            assert deleted == "Account Deleted!"
            page.wait_for_timeout(2000)

            page.wait_for_selector("//a[normalize-space()='Continue']").click()

        except Exception as e:
            pytest.fail(f"Login check failed: {e}")








