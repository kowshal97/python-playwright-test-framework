import pytest
from pathlib import Path

text_alert = []

def dialog_handler(dialog):
    text_alert.append(dialog.message)
    dialog.accept()


def test_contactus_form(home_page):
    page = home_page
    contact_form = page.wait_for_selector("//a[normalize-space()='Contact us']")
    contact_form.click()
    text = page.wait_for_selector("//h2[normalize-space()='Get In Touch']",state="visible",timeout=5000).text_content().strip()
    assert text == 'Get In Touch',f"{text}is not the expected text"
    print("Get in Touch is visible")

    name  = page.wait_for_selector("//input[@placeholder='Name']")
    name.fill('John')
    email = page.wait_for_selector("//input[@placeholder='Email']")
    email.fill('john@gmail.com')
    subject = page.wait_for_selector("//input[@placeholder='Subject']")
    subject.fill('need help')
    message = page.wait_for_selector("//textarea[@id='message']")
    message.fill('my name is john')

    upload_button = page.wait_for_selector("//input[@name='upload_file']")
    page.wait_for_timeout(2000)
    file_path = Path(r"C:\Users\Kowzs\Desktop\Resume\Non IT fields\Kowshal_Sugunarajah_Resume.pdf")
    upload_button.set_input_files(str(file_path))
    print("Upload file is successful")

    page.once("dialog", dialog_handler)
    submit = page.wait_for_selector("//input[@name='submit']")
    submit.click()

    if text_alert:
        print(f"Alert text:,{text_alert[0]}")

    page.wait_for_timeout(2000)

    success_locator = page.wait_for_selector("//div[@class='status alert alert-success']", state="visible",
                                             timeout=10000)
    print("visible",success_locator.is_visible())
    print("text",success_locator.text_content().strip())

    success_message = success_locator.text_content().strip()
    assert success_message == 'Success! Your details have been submitted successfully.', f"{success_message} is not the expected text"
    print("Success! Your details have been submitted successfully. is visible")










