import base_page
from locators import ProductPageLocators


class ProductPage(base_page.BasePage):

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def price_should_be_correct(self):
        price_msg = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
        price_card = self.browser.find_element(*ProductPageLocators.PRICE_IN_PRODUCT_CARD).text
        assert price_msg == price_card

    def name_should_be_correct(self):
        name_msg = self.browser.find_element(*ProductPageLocators.NAME_IN_MESSAGE).text
        name_card = self.browser.find_element(*ProductPageLocators.NAME_IN_PRODUCT_CARD).text
        assert name_msg == name_card

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
