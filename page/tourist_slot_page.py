import time

import pytest

from notification.locators import NotificationsLocators
from page.base_page import BasePage
from page.locators import TourismSlotLocators
from notification.notifications import Notifications


class TourismSlot(BasePage):
    def visa_tourism_slots(self, link):
        page = TourismSlot(self.browser, link)
        page.open()
        self.browser.implicitly_wait(3)

        notification = Notifications(self.browser, NotificationsLocators.MAIL_LINK)
        if page.is_not_element_present(*TourismSlotLocators.INFO_WINDOW):
            notification.send("The free slot is available at the link " + link)

        else:
            if (page.is_has_not_message_about_absence_slots()):
                #Given the high demand, the places available for the chosen service are sold out. Please check back frequently as new bookable appointments are added every week.
                notification.send("The free slot is available at the link " + link)

    def is_has_not_message_about_absence_slots(self):
        info_window = self.browser.find_element(*TourismSlotLocators.INFO_WINDOW).text
        return info_window != "!Given the high demand, the places available for the chosen service are sold out. Please check back frequently as new bookable appointments are added every week."
