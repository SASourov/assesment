import time

from appium import webdriver
from selenium.webdriver.common.by import By

from src.PlaceOrder.common_locator import CommonLocator
from src.PlaceOrder.manage_scrool import LayoutScrool

desired_caps = {}
desired_caps['platformVersion'] = '14'
desired_caps['udid'] = 'R5CRA0LGSFP'
desired_caps['deviceName'] = 'Glaxy A52s 5G'
desired_caps['testName'] = "Test 123"
desired_caps['appPackage'] = 'com.nopstation.nopcommerce.nopstationcart'
desired_caps['appActivity'] = 'com.bs.ecommerce.main.SplashScreenActivity'
desired_caps['platformName'] = 'android'
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
driver.implicitly_wait(20)

ls = LayoutScrool(driver)
cl = CommonLocator(driver)


read_and_accept = driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/btnAccept")
read_and_accept.click()

home_page = driver.find_element(By.XPATH,
                                    '//android.widget.FrameLayout[@content-desc="Home"]/android.widget.FrameLayout/android.widget.ImageView')
home_page.click()
time.sleep(3)

click_on_bed_mattress = driver.find_element(By.XPATH,
                                                '(//android.widget.ImageView[@content-desc="Placeholder"])[6]')

click_on_bed_mattress.click()

ls.scroll_down()
ls.scroll_down()
click_on_plus_icon = driver.find_element(By.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[4]/android.widget.Button[2]')
click_on_plus_icon.click()

cart_icon = driver.find_element(By.ID, 'com.nopstation.nopcommerce.nopstationcart:id/btnBuyNow')
cart_icon.click()

click_on_check_out = driver.find_element(By.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.RelativeLayout/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.TextView[2]')
click_on_check_out.click()

checkout_as_guest = driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/btnGuestCheckout")
checkout_as_guest.click()

set_frst_name = driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/etFirstName")
set_frst_name.send_keys("Mike")

set_lst_name = driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/etLastName")
set_lst_name.send_keys("Smith")

set_mail = driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/etEmail")
set_mail.send_keys("mike@mail.com")

select_country = driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/countrySpinner")
select_country.click()

select_country_value = driver.find_element(By.XPATH,
                                               "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[8]")
select_country_value.click()

set_company = driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/etCompanyName")
set_company.send_keys("BS 23 PLC")

set_city = driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/etCity")
set_city.send_keys("Dhaka City")

set_street = driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/etStreetAddress")
set_street.send_keys("Road 15, House21, Banani, Dhaka")

ls.scroll_down()
ls.scroll_down()

set_zip_code = driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/etZipCode")
set_zip_code.send_keys("1212")  # I Skipped some non-mandatory field

cl.click_continue_button()

click_next_day_year = driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/etCompanyName")
click_next_day_year.click()

cl.click_continue_button()
ls.scroll_down()
ls.scroll_down()
ls.scroll_down()
time.sleep(2)

cl.click_continue_button()
ls.scroll_down()
ls.scroll_down()
ls.scroll_down()
ls.scroll_down()
ls.scroll_down()
ls.scroll_down()

time.sleep(2)

cl.click_continue_button()
time.sleep(2)

# click_bck_arrow_btn = driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/back_arrow")
# click_bck_arrow_btn.click()
#
# click_continue = driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/md_button_positive")
# click_continue.click()

driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/btnContinue").click()

click_bck_arrow_btn = driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/back_arrow")
click_bck_arrow_btn.click()
print("Your order has been successfully processed!")


driver.quit()

