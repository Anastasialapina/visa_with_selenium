from notification.base_notification_page import BaseNotificationPage
from notification.locators import NotificationsLocators
from data import Data
import time

class Notifications(BaseNotificationPage):
    # send message with yandex email
    def send(self, text):
        link = NotificationsLocators.MAIL_LINK
        page = BaseNotificationPage(self.browser, link)
        page.open()
        page.login()

        # for check robot
        time.sleep(1)

        button_write = self.browser.find_element(*NotificationsLocators.WRITE_BUTTON)
        button_write.click()
        self.browser.implicitly_wait(3)

        write_text = self.browser.find_element(*NotificationsLocators.TEXT_FIELD)
        write_text.send_keys(text)

        receiver = self.browser.find_element(*NotificationsLocators.RECEIVER)
        receiver.send_keys(Data.EMAIL_FOR_SENDING_MESSAGE)

        send_button = self.browser.find_element(*NotificationsLocators.SEND_BUTTON)
        send_button.click()

        # for sending
        time.sleep(3)
