from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        put = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        put.click()     

    def checking_the_name_of_the_added_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        item_in_cart = self.browser.find_element(*ProductPageLocators.ITEM_IN_CART)
        assert product_name.text == item_in_cart.text, "The product name in the purchase message does not match the product" 

    def check_cart_value(self):
        basket_value = self.browser.find_element(*ProductPageLocators.BASKET_VALUE)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)   
        assert product_price.text == basket_value.text, "The price of the cart does not match the price of the product"