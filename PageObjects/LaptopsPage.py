import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from PageObjects.HpLaptop import Hplapy


class Laptop:
    hp_laptop_scroll = (By.XPATH, "//div[@class='image']//img[@alt='HP LP3065']")
    hp_laptop_required = (By.XPATH, "//img[@alt='HP LP3065']")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def scrolling(self):
        hplapy = self.driver.find_element(*Laptop.hp_laptop_scroll)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView()", hplapy)

    def required_lapy(self):
        self.wait.until(EC.element_to_be_clickable(Laptop.hp_laptop_required)).click()
        return Hplapy(self.driver, self.wait)




