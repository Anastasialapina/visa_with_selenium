from selenium.webdriver.common.by import By

class TourismSlotLocators():
    LOGIN_EMAIL = (By.ID, "login-email")
    LOGIN_PASSWORD = (By.ID, "login-password")
    BUTTON_TO_ENTRANCE = (By.CLASS_NAME, "button.primary.g-recaptcha")
    INFO_WINDOW = (By.CLASS_NAME, "jconfirm-content")
