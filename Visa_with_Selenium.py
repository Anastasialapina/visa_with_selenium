from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# send message with yandex email
def send(text):
    link = "https://passport.yandex.com.am/auth?retpath=https%3A%2F%2Fmail.yandex.com.am"

    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "login")
    input1.send_keys("your_email@yandex.ru")
    enter_button = browser.find_element(By.ID, "passp:sign-in")
    enter_button.click()
    browser.implicitly_wait(1)

    input2 = browser.find_element(By.NAME, "passwd")
    input2.send_keys("your_password")
    enter_button2 = browser.find_element(By.ID, "passp:sign-in")
    enter_button2.click()
    # for check robot
    time.sleep(1)

    write_link = "https://mail.yandex.com.am/#compose"
    browser.get(write_link)
    browser.implicitly_wait(3)

    write_text = browser.find_element(By.CSS_SELECTOR, "[title='Напишите что-нибудь']")
    write_text.send_keys(text)

    receiver = browser.find_element(By.CLASS_NAME, "composeYabbles")
    receiver.send_keys("your_email@yandex.ru")
    send_button = browser.find_element(By.CLASS_NAME, "Button2.Button2_view_action.Button2_size_l")
    send_button.click()

    time.sleep(2)
    browser.quit()

# tourism slot 1
def visa_slot1():

    link = "https://prenotami.esteri.it/Services/Booking/1151"

    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.ID, "login-email")
    input1.send_keys("your_email@yandex.ru")
    input2 = browser.find_element(By.ID, "login-password")
    input2.send_keys("your_password")
    button = browser.find_element(By.XPATH, "//button[text()='Avanti']")
    button.click()

    browser.implicitly_wait(3)
    try:
        info_window1 = browser.find_element(By.CLASS_NAME, "jconfirm-content")
    except NoSuchElementException:
        send("The free slot is available at the link https://prenotami.esteri.it/Services/Booking/1151")
    else:
        if (info_window1.text != "Al momento non ci sono date disponibili per il servizio richiesto"):
            send("The free slot is available at the link https://prenotami.esteri.it/Services/Booking/1151")

    browser.quit()

# tourism slot 2
def visa_slot2():

    link = "https://prenotami.esteri.it/Services/Booking/1258"

    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.ID, "login-email")
    input1.send_keys("your_email@yandex.ru")
    input2 = browser.find_element(By.ID, "login-password")
    input2.send_keys("your_password")
    button = browser.find_element(By.XPATH, "//button[text()='Avanti']")
    button.click()

    browser.implicitly_wait(3)

    try:
        info_window1 = browser.find_element(By.CLASS_NAME, "jconfirm-content")
    except NoSuchElementException:
        send("The free slot is available at the link https://prenotami.esteri.it/Services/Booking/1258")
    else:
        if (info_window1.text != "Al momento non ci sono date disponibili per il servizio richiesto"):
            send("The free slot is available at the link https://prenotami.esteri.it/Services/Booking/1258")

    browser.quit()

# before using this code you must register on the site https://prenotami.esteri.it/
if __name__ == "__main__":
    while True:
        visa_slot1()
        visa_slot2()
        # one time on 15 min
        time.sleep(900)
