from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Registration:
    firstname = (By.CSS_SELECTOR, "#input-firstname")
    lastname = (By.ID, "input-lastname")
    email = (By.ID, "input-email")
    telephone = (By.ID, "input-telephone")
    scroll = "window.scrollBy(0,500)"
    password = (By.ID, "input-password")
    password_confirm = (By.ID, "input-confirm")
    agree_to_terms = (By.NAME, "agree")
    continue_button = (By.XPATH, "//input[@value='Continue']")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def first_name(self, keys):
        first = self.wait.until(EC.presence_of_element_located(Registration.firstname))
        first.send_keys(keys)

    def last_name(self, keys):
        last = self.driver.find_element(*Registration.lastname)
        last.send_keys(keys)

    def enter_email(self, keys):
        email = self.driver.find_element(*Registration.email)
        email.send_keys(keys)

    def enter_mobile(self, keys):
        mobile = self.driver.find_element(*Registration.telephone)
        mobile.send_keys(keys)

    def scroll_down(self):
        return self.driver.execute_script(Registration.scroll)

    def input_password(self, keys):
        password = self.driver.find_element(*Registration.password)
        password.send_keys(keys)

    def confirm_password(self, keys):
        confirm = self.driver.find_element(*Registration.password_confirm)
        confirm.send_keys(keys)

    def agree_button(self):
        return self.driver.find_element(*Registration.agree_to_terms)

    def details_confirm(self):
        return self.wait.until(EC.element_to_be_clickable(Registration.continue_button))










