from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.RegistrationPage import Registration


class CheckoutPage:
    myaccount_button = (By.XPATH, "//span[contains(normalize-space(),'My Account')]")
    register_button = (By.LINK_TEXT, "Register")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def myaccount(self):
        return self.wait.until(EC.element_to_be_clickable(CheckoutPage.myaccount_button))

    def register(self):
        self.wait.until(EC.element_to_be_clickable(CheckoutPage.register_button)).click()
        return Registration(self.driver, self.wait)




