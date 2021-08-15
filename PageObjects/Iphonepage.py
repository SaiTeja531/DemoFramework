from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.LaptopsPage import Laptop


class Iphone:
    pictures = (By.XPATH, '//ul[@class="thumbnails"]/li[1]')
    next_click_button = (By.XPATH, "//button[@title='Next (Right arrow key)']")
    escape_button = (By.CSS_SELECTOR, "button[title='Close (Esc)']")
    no_of_iphones = (By.XPATH, '//input[@id="input-quantity"]')
    add_to_cart = (By.XPATH, "//button[@id='button-cart']")
    laptops = (By.LINK_TEXT, 'Laptops & Notebooks')
    All_laptops_Notebooks = (By.LINK_TEXT, 'Show All Laptops & Notebooks')

    def __init__(self, driver, wait, actions):
        self.driver = driver
        self.wait = wait
        self.actions = actions

    def iphone_pics(self):
        return self.wait.until(EC.element_to_be_clickable(Iphone.pictures))

    def sliding_pics(self):
        return self.wait.until(EC.element_to_be_clickable(Iphone.next_click_button))

    def escape_pics(self):
        return self.driver.find_element(*Iphone.escape_button)

    def required_iphones(self, items):
        phn = self.driver.find_element(*Iphone.no_of_iphones)
        phn.clear()
        phn.send_keys(items)

    def add_tocart(self):
        return self.wait.until(EC.element_to_be_clickable(Iphone.add_to_cart))

    def move_to_laptops(self):
        lapy = self.driver.find_element(*Iphone.laptops)
        self.actions.move_to_element(lapy).perform()
        self.wait.until(EC.element_to_be_clickable(Iphone.All_laptops_Notebooks)).click()
        return Laptop(self.driver, self.wait)











