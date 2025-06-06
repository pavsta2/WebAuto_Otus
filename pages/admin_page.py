"""Модуль методов взаимодействия с элементами страницы админки и ее локаторов"""
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdminPage(BasePage):
    CATALOG_LINK = By.ID, "menu-catalog"
    PRODUCTS_LINK = By.XPATH, "//*[@class='collapse show']/*[2]"
    ADD_NEW_BTN = By.XPATH, "//a[@title='Add New']"
    PRODUCT_NAME_FLD = By.ID, "input-name-1"
    META_TAG_FLD = By.ID, "input-meta-title-1"
    GENERAL_TAB = By.XPATH, "//a[@href='#tab-general']"
    DATA_TAB = By.XPATH, "//a[@href='#tab-data']"
    SEO_TAB = By.XPATH, "//a[@href='#tab-seo']"
    MODEL_FLD = By.ID, "input-model"
    KEYWORD_FLD = By.ID, "input-keyword-0-1"
    SAVE_NEW_PROD_BTN = By.XPATH, "//button[@form='form-product']"
    PRODUCT_LINE = By.XPATH, "//tbody/tr"
    DELETE_BTN = By.XPATH, "//button[@class='btn btn-danger']"
    PROD_TABLE_FIRST_LINE_NAME = By.XPATH, "//table/tbody/tr[1]/td[3]"

    @allure.step("Открытие страницы со списком продуктов")
    def enter_products_page(self):
        self.logger.info('%s: Entering product page' % self.class_name)
        self.click_elem(self.CATALOG_LINK)
        self.click_elem(self.PRODUCTS_LINK)

    def add_new_product(self, params: dict):
        """
        Функция добавления нового продукта в админке.
        В качестве параметра принимает словарь, в котором обязательны ключи со значениями:
        {
        'Product_name': 'value',
        'Meta_Tag_Title': 'value',
        'Model': 'value',
        'Keyword': 'value'
        }
        """
        prod_name = params['Product_name']
        with allure.step(f"Добавление нового продукта {prod_name}"):
            self.logger.info('%s: Adding new product %s' % (self.class_name, params['Product_name']))
            self.click_elem(self.ADD_NEW_BTN)
            self.click_elem(self.GENERAL_TAB)
            self.fill_the_field(self.PRODUCT_NAME_FLD, params['Product_name'])
            self.fill_the_field(self.META_TAG_FLD, params['Meta_Tag_Title'])
            self.click_elem(self.DATA_TAB)
            self.fill_the_field(self.MODEL_FLD, params['Model'])
            self.click_elem(self.SEO_TAB)
            self.fill_the_field(self.KEYWORD_FLD, params['Keyword'])
            self.click_elem(self.SAVE_NEW_PROD_BTN)

    @allure.step("Поиск элемента чекбокса строки продукта {prod_name}")
    def get_checkbox_elem_by_prod_name(self, prod_name: str):
        self.logger.info('%s: Getting checkbox element for product %s' % (self.class_name, prod_name))
        return self.get_element((By.XPATH, f'//tbody/tr/td[contains(text(), "{prod_name}")]/../*[1]'))

    @allure.step("Удаление продукта с названием {prod_name}")
    def del_product_by_name(self, prod_name):
        self.logger.info('%s: Deleting product: %s' % (self.class_name, prod_name))
        checkbox_el = self.get_checkbox_elem_by_prod_name(prod_name)
        checkbox_el.click()
        self.click_elem(self.DELETE_BTN)
        alert = self.driver.switch_to.alert
        alert.accept()

    @allure.step("Получение элемента первой строки таблицы продуктов")
    def get_first_line_prod_name(self):
        self.logger.info('%s: Getting first line in products table' % self.class_name)
        return self.get_element(self.PROD_TABLE_FIRST_LINE_NAME).text.split('\n')[0].replace('"', '')

