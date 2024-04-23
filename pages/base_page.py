from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import ProductPageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    def open(self):
        self.browser.get(self.url)
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    def is_not_element_present(self, how, what, timeout=4): #абстрактный метод, который проверяет, что элемент не появляется на странице в течение заданного времени: 
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    
    '''
    Если же мы хотим проверить, что какой-то элемент исчезает, 
    то следует воспользоваться явным ожиданием вместе 
    с функцией until_not, в зависимости от того, какой результат мы ожидаем: 
    is_not_element_present: упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый. 
    is_disappeared: будет ждать до тех пор, пока элемент не исчезнет. 
    '''
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
    
    
    def is_url_has_link(self, link):
        return str(link) in self.browser.current_url 
       
    
