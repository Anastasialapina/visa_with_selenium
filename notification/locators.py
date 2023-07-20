from selenium.webdriver.common.by import By
class NotificationsLocators():
    MAIL_LINK = "https://passport.yandex.com.am/auth?retpath=https%3A%2F%2Fmail.yandex.com.am"
    LOGIN_OF_MAIL = (By.NAME, "login")
    PASSWORD_OF_MAIL = (By.NAME, "passwd")
    ENTRANCE_BUTTON = (By.ID, "passp:sign-in")
    WRITE_BUTTON = (By.CLASS_NAME, "Button2.Button2_type_link.Button2_view_action.Button2_size_m."
                                   "Layout-m__compose--pTDsx.qa-LeftColumn-ComposeButton.ComposeButton-m__root--fP-o9")

    TEXT_FIELD = (By.CLASS_NAME, "cke_wysiwyg_div.cke_reset.cke_enable_context_menu.cke_editable.cke_editable_themed."
                                 "cke_contents_ltr.cke_htmlplaceholder")
    RECEIVER = (By.CLASS_NAME, "composeYabbles")
    SEND_BUTTON = (By.CLASS_NAME, "Button2.Button2_view_action.Button2_size_l")
