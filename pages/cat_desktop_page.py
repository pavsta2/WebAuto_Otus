"""Модуль методов взаимодействия с элементами страницы каталога и ее локаторов"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CatDesktopPage(BasePage):
    CATALOG_TITLE = By.CSS_SELECTOR, "h2"
    SELECT_SORT_FLD = By.ID, "input-sort"
    SELECT_LIMIT_FLD = By.ID, "input-limit"
    BRDCRUMBS_ELEM = By.CLASS_NAME, "breadcrumb-item"
    ALL_PRICES = By.XPATH, "//span[@class='price-new']"
