from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.product_page import ProductPage
import time,pytest
from pages.login_page import LoginPage

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()   
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_see_forms(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()

@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer=2):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.tap_to_button()
    time.sleep(1)
    page.solve_quiz_and_get_code()
    page.match_text()
    time.sleep(150)

@pytest.mark.need_review
@pytest.mark.xfail(reason="its not a bug")    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, promo_offer=2):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.tap_to_button()
    time.sleep(1)
    page.solve_quiz_and_get_code()
    page.have_no_success_message_after_adding_product_to_basket()

@pytest.mark.need_review
def test_guest_cant_see_success_message(browser, promo_offer=2): 
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    # page.tap_to_button()
    time.sleep(1)
    # page.solve_quiz_and_get_code()
    page.have_no_success_message()

@pytest.mark.need_review
@pytest.mark.xfail(reason="its not a bug")
def test_message_disappeared_after_adding_product_to_basket(browser, promo_offer=2):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.tap_to_button()
    time.sleep(1)
    page.solve_quiz_and_get_code()
    page.have_no_success_message_after_adding_product_to_basket_with_disappeared_func()



