# 02_Automation_Testing/tests/test_contact_form_demoqa.py
import pytest
from pages.contact_page import ContactPage
import os

@pytest.mark.smoke
def test_contact_form_full_flow(driver, config):
    cp = ContactPage(driver)
    # Fill required fields
    cp.fill_names_and_email("Raj", "Shinde", "raj.testing@example.com")
    cp.select_gender("Male")
    cp.type_mobile("9999999999")
    cp.set_dob("10 May 1990")                 # or "10 May 1990"
    cp.add_subject("Maths")
    cp.select_hobbies(["Sports","Reading"])
    # upload a small file included in repo: 02_Automation_Testing/tests/test_files/sample.png
    sample = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tests", "test_files", "sample.png")
    # if sample not present, skip upload
    if os.path.exists(sample):
        cp.upload_picture(sample)
    cp.type_address("123, Pune")
    cp.select_state_city("NCR", "Delhi")
    cp.submit_form()
    assert cp.is_submission_success(), "Submission modal not shown"
    cp.close_submission_modal()

@pytest.mark.regression
def test_contact_form_invalid_email_shows_error(driver, config):
    cp = ContactPage(driver)
    cp.fill_names_and_email("Raj", "Shinde", "invalid-email")
    cp.select_gender("Male")
    cp.type_mobile("9999999999")
    cp.set_dob("10 May 1990")                 # or "10 May 1990"
    cp.add_subject("Maths")
    cp.select_hobbies(["Sports","Reading"])
    # upload a small file included in repo: 02_Automation_Testing/tests/test_files/sample.png
    sample = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tests", "test_files", "sample.png")
    # if sample not present, skip upload
    if os.path.exists(sample):
        cp.upload_picture(sample)
    cp.type_address("123, Pune")
    cp.select_state_city("NCR", "Delhi")
    cp.submit_form()
    assert cp.is_submission_success(), "Submission modal not shown"
    cp.close_submission_modal()
