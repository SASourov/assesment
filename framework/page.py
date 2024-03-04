from selenium.webdriver.common.by import By


class AddProductsInCart:
    def __init__(self, driver):
        self.driver = driver

        self.read_and_accept = (By.ID, "com.nopstation.nopcommerce.nopstationcart:id/btnAccept")
        self.home_page = (By.XPATH,
                          '//android.widget.FrameLayout[@content-desc="Home"]/android.widget.FrameLayout/android.widget.ImageView')
        self.bed_mattress = (By.XPATH, '(//android.widget.ImageView[@content-desc="Placeholder"])[6]')
        self.plus_icon = (By.XPATH,
                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[4]/android.widget.Button[2]')
        self.cart_icon = (By.ID, 'com.nopstation.nopcommerce.nopstationcart:id/btnBuyNow')

    def click_on_raed_and_accept(self):
        self.driver.find_element(*self.read_and_accept).click()

    def click_home_page(self):
        self.driver.find_element(*self.home_page).click()

    def click_on_bed_mattress(self):
        self.driver.find_element(*self.bed_mattress).click()

    def click_on_plus_icon(self):
        self.driver.find_element(*self.plus_icon).click()

    def click_on_crt_btn(self):
        self.driver.find_element(*self.cart_icon).click()


class PlaceOrderAsGuest:
    def __init__(self, driver):
        self.driver = driver

        self.read_and_accept = (By.ID, "com.nopstation.nopcommerce.nopstationcart:id/btnAccept")
        self.check_out = (By.XPATH,
                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.RelativeLayout/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.TextView[2]')
        self.check_out_as_guest = (By.ID, "com.nopstation.nopcommerce.nopstationcart:id/btnGuestCheckout")
        self.frst_name = (By.ID, "com.nopstation.nopcommerce.nopstationcart:id/etFirstName")
        self.lst_name = (By.ID, "com.nopstation.nopcommerce.nopstationcart:id/etLastName")
        self.email = (By.ID, "com.nopstation.nopcommerce.nopstationcart:id/etEmail")
        self.country = (By.ID, "com.nopstation.nopcommerce.nopstationcart:id/countrySpinner")
        self.country_value = (By.XPATH,
                              "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[8]")
        self.company_name = (By.ID, "com.nopstation.nopcommerce.nopstationcart:id/etCompanyName")
        self.city_name = (By.ID, "com.nopstation.nopcommerce.nopstationcart:id/etCity")
        self.street_num = (By.ID, "com.nopstation.nopcommerce.nopstationcart:id/etStreetAddress")
        self.zip_code = (By.ID, "com.nopstation.nopcommerce.nopstationcart:id/etZipCode")
        self.next_day_air = (By.ID, "com.nopstation.nopcommerce.nopstationcart:id/etCompanyName")
        self.next_button = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.widget.Button")
        self.confirm_button = (By.ID, "com.nopstation.nopcommerce.nopstationcart:id/btnContinue")
        self.bck_arw_button = (By.ID, "com.nopstation.nopcommerce.nopstationcart:id/back_arrow")

    def click_on_raed_and_accept(self):
        self.driver.find_element(*self.read_and_accept).click()

    def click_on_check_out_btn(self):
        self.driver.find_element(*self.check_out).click()

    def click_as_guest_btn(self):
        self.driver.find_element(*self.check_out_as_guest).click()

    def set_frst_name(self, frst_name):
        self.driver.find_element(*self.frst_name).send_keys(frst_name)

    def set_last_name(self, lst_name):
        self.driver.find_element(*self.lst_name).send_keys(lst_name)

    def set_email(self, mail):
        self.driver.find_element(*self.email).send_keys(mail)

    def click_country_list(self):
        self.driver.find_element(*self.country).click()

    def set_country(self):
        self.driver.find_element(*self.country_value).click()

    def set_company_name(self, company):
        self.driver.find_element(*self.company_name).send_keys(company)

    def set_city_name(self, city):
        self.driver.find_element(*self.city_name).send_keys(city)

    def set_street(self, street):
        self.driver.find_element(*self.street_num).send_keys(street)

    def set_zip_code(self, zip):
        self.driver.find_element(*self.zip_code).send_keys(zip)

    def click_nxt_day_air(self):
        self.driver.find_element(*self.next_day_air).click()

    def click_nxt_btn(self):
        self.driver.find_element(*self.next_button).click()

    def click_confirm_btn(self):
        self.driver.find_element(*self.confirm_button).click()
