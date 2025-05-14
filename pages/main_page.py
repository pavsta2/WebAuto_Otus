"""Модуль методов взаимодействия с элементами главной страницы и ее локаторов"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    CAROUSEL_EL = By.CLASS_NAME, "carousel-indicators"
    SEARCH_FIELD = By.NAME, "search"
    CART_BTN = By.CSS_SELECTOR, "#header-cart > div > button"
    NAV_PANEL = By.CSS_SELECTOR, ".nav-item"
    ALL_PROD_CARDS = By.XPATH, "//a/img[@class='img-fluid']"
    ALL_PRICES = By.XPATH, "//span[@class='price-new']"
    SEARCH_BTN = By.XPATH, "//button[@class='btn btn-light btn-lg']"
    PROD_NAME_IN_CARD = By.XPATH, "//h4"

    def search_for_product(self, prod_name: str):
        self.fill_the_field(self.SEARCH_FIELD, prod_name)
        self.click_elem(self.SEARCH_BTN)
