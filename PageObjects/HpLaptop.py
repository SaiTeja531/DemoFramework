from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.checkoutPage import CheckoutPage


class Hplapy:
    calender_element = (By.XPATH, "//i[@class='fa fa-calendar']")
    calender_next_button = (By.XPATH, "//th[@class='next']")
    year = (By.XPATH, "//div[@class='datepicker']//*//th[@class='picker-switch']")
    date = (By.XPATH, '//td')
    add_to_cart_button = (By.XPATH, "//button[@id='button-cart']")
    total_cart = (By.XPATH, "//span[@id='cart-total']")
    check_out_button = (By.XPATH, '//body//header//a[2]')

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def calender_selection(self):
        return self.wait.until(EC.element_to_be_clickable(Hplapy.calender_element))

    def next_button_in_calender(self, which_year):
        next_button = self.wait.until(EC.element_to_be_clickable(Hplapy.calender_next_button))
        yea = self.driver.find_element(*Hplapy.year)
        while yea.text != which_year:
            next_button.click()

    def date_selection(self, pick_date):
        cal = self.wait.until(EC.presence_of_all_elements_located(Hplapy.date))
        for date in cal:
            if pick_date in date.text:
                date.click()
                break

    def scrolling_body(self):
        return self.driver.execute_script("window.scrollTo(0,document.scrollHeight)")

    def add_to_cart(self):
        return self.wait.until(EC.element_to_be_clickable(Hplapy.add_to_cart_button))

    def checking_total_cart(self):
        return self.wait.until(EC.element_to_be_clickable(Hplapy.total_cart))

    def checkout(self):
        self.wait.until(EC.element_to_be_clickable(Hplapy.check_out_button)).click()
        return CheckoutPage(self.driver, self.wait)

    







