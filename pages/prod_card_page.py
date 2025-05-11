"""Модуль методов взаимодействия с элементами страницы карточки товара и ее локаторов"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProdCardPage(BasePage):
    LIKE_BTN = By.XPATH, "//button[@type='submit']"
    TEXTAREA_FLD = By.XPATH, "//textarea[@name='option[209]']"
    ADD_TO_CART_BTN = By.ID, "button-cart"
    DESCR_TAB = By.XPATH, "//a[@href='#tab-description']"
    COLOR_SELECT = By.NAME, "option[226]"
    CART_POP_UP = By.XPATH, "//div/div/a"

    def add_to_cart_color_select(self, locator: tuple, color_ind=0):
        self.select_opt_by_ind(locator, color_ind)
        self.click_elem(self.ADD_TO_CART_BTN)
