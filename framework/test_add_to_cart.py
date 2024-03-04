import time
from lib2to3.pgen2 import driver

from appium import webdriver
import pytest
from selenium.webdriver.common.by import By

from framework.page import AddProductsInCart, PlaceOrderAsGuest
from src.PlaceOrder.common_locator import CommonLocator
from src.PlaceOrder.manage_scrool import LayoutScroll

desired_caps = {}
desired_caps['platformVersion'] = '14'
desired_caps['udid'] = 'R5CRA0LGSFP'
desired_caps['deviceName'] = 'Glaxy A52s 5G'
desired_caps['testName'] = "Test 123"
desired_caps['appPackage'] = 'com.nopstation.nopcommerce.nopstationcart'
desired_caps['appActivity'] = 'com.bs.ecommerce.main.SplashScreenActivity'
desired_caps['platformName'] = 'android'


class Test_001:
    def test_add_to_cart(self):
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(20)
        self.ls = LayoutScroll(self.driver)
        self.adtocrt = AddProductsInCart(self.driver)
        self.adtocrt.click_on_raed_and_accept()
        self.adtocrt.click_home_page()
        self.adtocrt.click_on_bed_mattress()
        time.sleep(2)
        self.ls.scroll_down()
        self.adtocrt.click_on_plus_icon()
        self.adtocrt.click_on_crt_btn()
        self.cl = CommonLocator(self.driver)
        self.po = PlaceOrderAsGuest(self.driver)
        self.po.click_on_check_out_btn()
        self.po.click_as_guest_btn()
        self.po.set_frst_name("Mike")
        self.po.set_last_name("Hasi")
        self.po.set_email("mike@mai.com")
        self.po.click_country_list()
        self.po.set_country()
        self.po.set_company_name("Test Company LTD")
        self.po.set_city_name("Dhaka")
        self.po.set_street("Road#11, House#11, Banani")
        self.ls.scroll_down()
        self.po.set_zip_code("1212")
        self.cl.click_continue_button()
        self.po.click_nxt_day_air()
        self.ls.scroll_down()
        self.cl.click_continue_button()
        self.ls.scroll_down()
        time.sleep(2)
        self.cl.click_continue_button()
        self.ls.scroll_down()
        self.ls.scroll_down()
        self.ls.scroll_down()
        self.ls.scroll_down()
        self.ls.scroll_down()
        self.ls.scroll_down()
        time.sleep(2)
        self.cl.click_continue_button()
        self.po.click_nxt_btn()
        self.po.click_confirm_btn()

        expected_text = self.driver.find_element(By.ID,
                                                 "com.nopstation.nopcommerce.nopstationcart:id/md_text_title").text

        if expected_text == "Thank you":
            assert True
            print("Test Passed\n Your Expected Message is : Your order has been successfully processed!")

        else:
            assert False
