"""Класс элемента изменения валюты в хэдере"""
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CurrencyElement(BasePage):
    CURRENCY_BTN = By.XPATH, "//ul[@class='list-inline']"

    @allure.step("Изменение валюты на {currency}")
    def change_currency(self, currency:str):
        self.logger.info('%s: Changing currency in a header to %s' % (self.class_name, currency))
        # получаем элемент кнопки выбора валюты и нажимаем
        self.click_elem(self.CURRENCY_BTN)
        # находим элемент с опцией валюты ЕВРО и нажимаем
        self.click_elem((By.XPATH, f"//a[@href={currency}]"))