from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEV_SHOPPING_CART = (By.XPATH, "//span/a[@class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT_REGISTER = (By.XPATH, "//div/input[@name='registration-email']")
    PASSWORD_INPUT_REGISTER = (By.XPATH, "//div/input[@name='registration-password1']")
    CONFIRM_PASSWORD_INPUT_REGISTER = (By.XPATH, "//div/input[@name='registration-password2']")
    REGISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")
    REGISTER_OK_NOTIFICATION = (By.XPATH, "//div/i[@class='icon-ok-sign']")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME = (By.XPATH, "id('content_inner')/article/div/div[2]/h1")
    PRODUCT_PRICE = (By.XPATH, "id('content_inner')/article/div/div[2]/p[@class='price_color']")
    ITEM_IN_CART = (By.XPATH, "id('messages')/div/div/strong")
    BASKET_VALUE = (By.XPATH, "id('messages')/div[3]/div/p/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]")

class BasketPageLocators():
     BASKET_ITEMS = (By.XPATH, "//div[@class='basket-items']")
     EMPTY_CART_NOTIFICATION = (By.XPATH, "//div[@id='content_inner']/p")