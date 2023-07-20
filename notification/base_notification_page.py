from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from notification.locators import NotificationsLocators
from selenium.webdriver.support import expected_conditions as EC
from data import Data

class BaseNotificationPage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def login(self):
        login = self.browser.find_element(*NotificationsLocators.LOGIN_OF_MAIL)
        login.send_keys(*Data.EMAIL_FOR_SENDING_MESSAGE)
        enter_button = self.browser.find_element(*NotificationsLocators.ENTRANCE_BUTTON)
        enter_button.click()
        self.browser.implicitly_wait(1)

        password = self.browser.find_element(*NotificationsLocators.PASSWORD_OF_MAIL)
        password.send_keys(*Data.PASSWORD_OF_EMAIL_FOR_SENDING_MESSAGE)
        enter_button = self.browser.find_element(*NotificationsLocators.ENTRANCE_BUTTON)
        enter_button.click()

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
