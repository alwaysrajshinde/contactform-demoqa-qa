# 02_Automation_Testing/pages/contact_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
import os, time

class ContactPage(BasePage):
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    # labels are clickable; we prefer to click label via robust BasePage.click
    GENDER_MALE_LABEL = (By.XPATH, "//label[text()='Male']")
    GENDER_FEMALE_LABEL = (By.XPATH, "//label[text()='Female']")
    MOBILE = (By.ID, "userNumber")
    DOB_INPUT = (By.ID, "dateOfBirthInput")
    SUBJECTS_INPUT = (By.ID, "subjectsInput")
    HOBBIES_SPORTS = (By.XPATH, "//label[text()='Sports']")
    HOBBIES_READING = (By.XPATH, "//label[text()='Reading']")
    HOBBIES_MUSIC = (By.XPATH, "//label[text()='Music']")
    PICTURE = (By.ID, "uploadPicture")
    ADDRESS = (By.ID, "currentAddress")
    STATE_INPUT = (By.ID, "react-select-3-input")
    CITY_INPUT = (By.ID, "react-select-4-input")
    SUBMIT = (By.ID, "submit")
    MODAL = (By.CSS_SELECTOR, "div.modal-content")
    MODAL_CLOSE = (By.ID, "closeLargeModal")

    def open_contact(self):
        # base_url is opened by fixture; ensure we are on the form
        if self.driver.current_url.strip() == "":
            self.open(self.config.get('base_url'))

    def fill_names_and_email(self, first, last, email):
        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.EMAIL, email)

    def select_gender(self, gender="Male"):
        # click the label (robust click handles interception)
        if gender.lower().startswith("m"):
            self.click(self.GENDER_MALE_LABEL)
        else:
            self.click(self.GENDER_FEMALE_LABEL)

    def type_mobile(self, mobile):
        self.type(self.MOBILE, mobile)

    def set_dob(self, date_str):
        el = self.find(self.DOB_INPUT)
        el.click()
        el.send_keys(Keys.CONTROL + "a")
        el.send_keys(date_str)
        el.send_keys(Keys.ENTER)
        time.sleep(0.3)

    def add_subject(self, subject):
        el = self.find(self.SUBJECTS_INPUT)
        el.send_keys(subject)
        time.sleep(0.25)
        el.send_keys(Keys.ENTER)
        time.sleep(0.2)

    def select_hobbies(self, hobbies:list):
        for h in hobbies:
            if h.lower() == "sports":
                self.click(self.HOBBIES_SPORTS)
            elif h.lower() == "reading":
                self.click(self.HOBBIES_READING)
            elif h.lower() == "music":
                self.click(self.HOBBIES_MUSIC)

    def upload_picture(self, file_path):
        if not os.path.isabs(file_path):
            file_path = os.path.abspath(file_path)
        # send_keys on input works; ensure file exists
        if os.path.exists(file_path):
            self.find(self.PICTURE).send_keys(file_path)
            time.sleep(0.3)
        else:
            raise FileNotFoundError(f"Upload file not found: {file_path}")

    def type_address(self, address):
        self.type(self.ADDRESS, address)

    def select_state_city(self, state, city):
        # type into react-select inputs and press ENTER
        si = self.find(self.STATE_INPUT)
        si.send_keys(state)
        time.sleep(0.3)
        si.send_keys(Keys.ENTER)
        time.sleep(0.3)
        ci = self.find(self.CITY_INPUT)
        ci.send_keys(city)
        time.sleep(0.3)
        ci.send_keys(Keys.ENTER)
        time.sleep(0.3)

    def submit_form(self):
        # try to ensure submit is visible and not blocked
        self.click(self.SUBMIT)
        time.sleep(1)

    def is_submission_success(self):
        return self.is_visible(self.MODAL)

    def close_submission_modal(self):
        if self.is_submission_success():
            self.click(self.MODAL_CLOSE)
            time.sleep(0.3)
