from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(3) > .alertinner > p > strong')
    PRICE_IN_PRODUCT_CARD = (By.CSS_SELECTOR, '.product_main > p.price_color')
    NAME_IN_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    NAME_IN_PRODUCT_CARD = (By.CSS_SELECTOR, '.product_main > h1')
    
