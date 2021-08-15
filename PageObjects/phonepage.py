from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.Iphonepage import Iphone


class PhonePage:
    iphone = (By.XPATH, '//div//a[@href="http://tutorialsninja.com/demo/'
                                        'index.php?route=product/product&path=24&product_id=40"]'
                                        '//img')

    def __init__(self, driver, wait, actions):
        self.driver = driver
        self.wait = wait
        self.actions = actions

    def phone(self):
        self.wait.until(EC.element_to_be_clickable(PhonePage.iphone)).click()
        return Iphone(self.driver, self.wait, self.actions)
