from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

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




