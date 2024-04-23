from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM_LOCATOR = (By.XPATH, "//form[@id='login_form']")
    REGISTER_FORM_LOCATOR = (By.XPATH, "//form[@id='register_form']")
    LOGIN_USERNAME_LOCATOR = (By.XPATH, "//input[@id='id_login-username']")
    LOGIN_PASSWORD_LOCATOR = (By.XPATH, "//input[@id='id_login-password']")

class ProductPageLocators():
    ADD_TO_CART_BUTTON_LOCATOR = (By.CSS_SELECTOR, '#add_to_basket_form [type="submit"]')
    SEE_A_BUSKET = (By.XPATH, "//div[contains(@class, 'basket-mini')]/span[@class='btn-group']/a")
    PRODUCT_NAME_AFTER_ADDING_IT_TO_CART = (By.XPATH, '//div[@id="messages"]/div[1]/div[@class="alertinner "]/strong')
    CART_PRICE = (By.XPATH, '//div[@id="messages"]/div[3]/div[@class="alertinner "]/p/strong')
    PRODUCT_NAME_IN_MAIN_PAGE = (By.XPATH, '//div[contains(@class,"product_main")]/h1')
    PRODUCT_PRICE_IN_MAIN_PAGE = (By.XPATH, '//div[contains(@class,"product_main")]/p[contains(@class, "price_color")]')
