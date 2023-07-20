from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from page.locators import TourismSlotLocators
from selenium.webdriver.support import expected_conditions as EC
from data import Data

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def login(self):
        email = self.browser.find_element(*TourismSlotLocators.LOGIN_EMAIL)
        email.send_keys(*Data.EMAIL_FOR_VISA_SITE)
        password = self.browser.find_element(*TourismSlotLocators.LOGIN_PASSWORD)
        password.send_keys(*Data.PASSWORD_FOR_VISA_SITE)
        button = self.browser.find_element(*TourismSlotLocators.BUTTON_TO_ENTRANCE)
        button.click()

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
