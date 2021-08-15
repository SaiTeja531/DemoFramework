from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.phonepage import PhonePage


class Homepage:
    phone = (By.LINK_TEXT, "Phones & PDAs")

    def __init__(self, driver, wait, actions):
        self.driver = driver
        self.wait = wait
        self.actions = actions

    def phone_tab(self):
        self.wait.until(EC.element_to_be_clickable(Homepage.phone)).click()
        ph = PhonePage(self.driver, self.wait, self.actions)
        return ph
