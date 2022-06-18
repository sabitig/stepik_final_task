from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def checking_if_the_cart_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "there are items in the cart when they should not be"        

    def there_is_an_empty_cart_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_CART_NOTIFICATION), "Missing empty cart message"