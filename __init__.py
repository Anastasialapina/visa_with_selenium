from selenium import webdriver
from link import MainLink
from page.tourist_slot_page import TourismSlot
import time

# before using this code you must register on the site https://prenotami.esteri.it/
class Main():
    def __init__(self):
        self.browser = webdriver.Chrome()

    def find_free_tourist_slot(self, link):
        page = TourismSlot(self.browser, MainLink.GLOBAL_LINK)
        page.open()
        page.login()
        page.visa_tourism_slots(link)
        self.destructor()

    def destructor(self):
        self.browser.quit()

if __name__ == "__main__":
    while True:
        Main().find_free_tourist_slot(MainLink.TOURISM_LINK1)
        Main().find_free_tourist_slot(MainLink.TOURISM_LINK2)
        # one time on 15 min
        time.sleep(900)
