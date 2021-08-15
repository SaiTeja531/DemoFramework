import time
from Utilities.BaseClass import BossClass
from PageObjects.HomePage import Homepage


class TestProject(BossClass):

    def test_ecommerce(self):
        # Clicking on phone menu
        home = Homepage(self.driver, self.wait, self.actions)
        phone = home.phone_tab()
        # clicking on iphone
        ph = phone.phone()
        # clicking on picture
        ph.iphone_pics().click()
        # sliding through pictures
        next_click = ph.sliding_pics()
        for i in range(0, 5):
            next_click.click()
            time.sleep(2)
        ph.escape_pics().click()
        self.how_much_time_u_want_to_stop_the_script(2)
        # required iphones 2
        ph.required_iphones(4)
        # add to cart
        ph.add_tocart().click()
        self.how_much_time_u_want_to_stop_the_script(2)
        lp = ph.move_to_laptops()
        # Laptops page
        lp.scrolling()
        self.how_much_time_u_want_to_stop_the_script(2)
        hp = lp.required_lapy()
        self.how_much_time_u_want_to_stop_the_script(2)
        hp.calender_selection().click()
        self.how_much_time_u_want_to_stop_the_script(2)
        # pass which year u want to select
        hp.next_button_in_calender("February 2015")
        self.how_much_time_u_want_to_stop_the_script(3)
        # Date selection
        hp.date_selection("24")
        self.how_much_time_u_want_to_stop_the_script(2)
        hp.scrolling_body()
        self.how_much_time_u_want_to_stop_the_script(3)
        hp.add_to_cart().click()
        self.how_much_time_u_want_to_stop_the_script(2)
        hp.checking_total_cart().click()
        self.how_much_time_u_want_to_stop_the_script(2)
        checkitout = hp.checkout()
        self.how_much_time_u_want_to_stop_the_script(2)
        # checkout page
        checkitout.myaccount().click()
        self.how_much_time_u_want_to_stop_the_script(2)
        register = checkitout.register()
        self.how_much_time_u_want_to_stop_the_script(2)
        # Registration page
        register.first_name("mahesh")
        self.how_much_time_u_want_to_stop_the_script(2)
        register.last_name("chiranjeevi")
        self.how_much_time_u_want_to_stop_the_script(2)
        register.enter_email("mahesh@gmail.com")
        self.how_much_time_u_want_to_stop_the_script(2)
        register.enter_mobile("7886978697")
        self.how_much_time_u_want_to_stop_the_script(2)
        register.scroll_down()
        self.how_much_time_u_want_to_stop_the_script(2)
        register.input_password("mahesh123")
        self.how_much_time_u_want_to_stop_the_script(2)
        register.confirm_password("mahesh123")
        self.how_much_time_u_want_to_stop_the_script(2)
        register.agree_button().click()
        self.how_much_time_u_want_to_stop_the_script(2)
        register.details_confirm().click()
        self.driver.get_screenshot_as_png()

