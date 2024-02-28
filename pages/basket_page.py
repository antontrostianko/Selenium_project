from selenium.webdriver.common.by import By

from base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_should_be_empty(self):
        self.no_items_in_basket()
        self.should_be_empty_message()

    def no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_DIV), 'Basket is not empty'

    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE)