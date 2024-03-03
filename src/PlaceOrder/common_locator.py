from selenium.webdriver.common.by import By


class CommonLocator:

    def __init__(self, driver):
        self.driver = driver

    def click_continue_button(self):
        click_confirm_button = self.driver.find_element(By.ID,
                                                        "com.nopstation.nopcommerce.nopstationcart:id/btnContinue")
        click_confirm_button.click()
