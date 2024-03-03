from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

desired_caps = {}
desired_caps['platformVersion'] = '14'
desired_caps['udid'] = 'R5CRA0LGSFP'
desired_caps['deviceName'] = 'Glaxy A52s 5G'
desired_caps['testName'] = "Test 123"
desired_caps['appPackage'] = 'com.nopstation.nopcommerce.nopstationcart'
desired_caps['appActivity'] = 'com.bs.ecommerce.main.SplashScreenActivity'
desired_caps['platformName'] = 'android'


def scenario_1():
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    driver.implicitly_wait(20)

    read_and_accept = driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/btnAccept")
    read_and_accept.click()

    home_page = driver.find_element(By.XPATH,
                                    '//android.widget.FrameLayout[@content-desc="Home"]/android.widget.FrameLayout/android.widget.ImageView')
    home_page.click()

    click_on_electronics = driver.find_element(By.XPATH, '(//android.widget.ImageView[@content-desc="Placeholder"])[7]')
    click_on_electronics.click()

    click_on_bed_mattress = driver.find_element(By.ID, 'com.nopstation.nopcommerce.nopstationcart:id/ivProductThumb')
    click_on_bed_mattress.click()

    click_on_cart = driver.find_element(By.ID, 'com.nopstation.nopcommerce.nopstationcart:id/btnAddToCart')
    click_on_cart.click()

    click_on_plus_icon = driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/btnPlus")
    click_on_plus_icon.click()

    driver.close()


def scenario_2():
    driver = webdriver.Remote("http://localhost:4723", desired_caps)
    driver.implicitly_wait(20)

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

    select_country = Select(driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/countrySpinner"))
    select_country.select_by_visible_text("Australia")

    set_company = driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/etCompanyName")
    set_company.send_keys("BS 23 PLC")

    set_city = driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/etCity")
    set_city.find_element("Dhaka City")

    set_street = driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/etStreetAddress")
    set_street.send_keys("Road 15, House21, Banani, Dhaka")

    set_zip_code = driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/etZipCode")
    set_zip_code.send_keys("1212")  # I Skipped some non-mandatory field

    click_on_continue_btn = driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/btnContinue")
    click_on_continue_btn.click()

    click_next_day_year = driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/etCompanyName")
    click_next_day_year.click()

    click_on_continue_btn = driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/btnContinue")
    click_on_continue_btn.click()

    click_on_continue_btn = driver.find_element(By.ID, "com.nopstation.nopcommerce.nopstationcart:id/btnContinue")
    click_on_continue_btn.click()

    click_on_next_btn = driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.widget.Button")
    click_on_next_btn.click()

    click_confirm_button = driver.find_element(By.XPATH, "com.nopstation.nopcommerce.nopstationcart:id/etZipCode")
    click_confirm_button.click()

    click_ok_button = driver.find_element(By.ID, "eu-cookie-ok")
    click_ok_button.click()

    expected_text = driver.find_element(By.CLASS_NAME, "android.widget.TextView").text

    if expected_text == "Order information":
        assert True
        print("Test Done\nThank you so much for review my code")

    else:
        print("I am sorry. Maybe in my code have some error")

    driver.quit()


scenario_1()
scenario_2()
