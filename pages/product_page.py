from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import math



class ProductPage(BasePage):
    # def should_be_login_page(self):
    #     self.should_be_login_url()
    #     self.should_be_login_form()
    #     self.should_be_register_form()

    # def should_be_login_url(self):
    #     assert self.is_url_has_link("login"),  "there are have no login page url"

    # def should_be_login_form(self):
    #     assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LOCATOR), "Login form is not presented"
        
    # def should_be_register_form(self):
    #     assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_LOCATOR), "Register form is not presented"
    # def go_to_login_page(self):
    #     link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     link.click()
    #     return LoginPage(browser=self.browser, url=self.browser.current_url) 
    def tap_to_button(self):
        try: 
            button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON_LOCATOR)
            button.click()
        except:
            print("error in tap_to_button_func")
    def tap_to_busket_button(self):
        try: 
            button = self.browser.find_element(*ProductPageLocators.SEE_A_BUSKET)
            button.click()
        except:
            print("error in tap_to_button_func")

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            WebDriverWait(self.browser, 3).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def match_text(self):
        try:
            product_name_text_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_AFTER_ADDING_IT_TO_CART).text
            cart_price_text_in_message = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
            product_name_text_in_main_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MAIN_PAGE).text
            product_price_text_in_main_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MAIN_PAGE).text
            if product_name_text_in_message == product_name_text_in_main_page and cart_price_text_in_message == product_price_text_in_main_page:
                print("all tests are passed, texts in page match each other")
            else:
                print(f'product_name_text_in_message: {product_name_text_in_message}')
                print(f'cart_price_text_in_message: {cart_price_text_in_message}')
                print(f'product_name_text_in_main_page: {product_name_text_in_main_page}')
                print(f'product_price_text_in_main_page: {product_price_text_in_main_page}')
                print(self.browser.current_url)
        except:
            print("error in match text func")
    
    def have_no_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_AFTER_ADDING_IT_TO_CART), "Success message is presented"
    def have_no_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_AFTER_ADDING_IT_TO_CART), "Success message is presented"
    def have_no_success_message_after_adding_product_to_basket_with_disappeared_func(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_AFTER_ADDING_IT_TO_CART), "Success message is presented"
    

        


