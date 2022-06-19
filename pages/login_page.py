from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "there is no login substring in the current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form field not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form field not present"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_INPUT_REGISTER).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_REGISTER).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_INPUT_REGISTER).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
        assert self.browser.find_element(*LoginPageLocators.REGISTER_OK_NOTIFICATION), "Регистрации не произошло"

        