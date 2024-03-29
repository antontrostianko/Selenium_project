from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini > span > a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    ITEM_DIV = (By.CSS_SELECTOR, 'basket-items')
    EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')
    REPEAT_PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form > button')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(3) > .alertinner > p > strong')
    PRICE_IN_PRODUCT_CARD = (By.CSS_SELECTOR, '.product_main > p.price_color')
    NAME_IN_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    NAME_IN_PRODUCT_CARD = (By.CSS_SELECTOR, '.product_main > h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
