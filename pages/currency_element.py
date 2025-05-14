"""Класс элемента изменения валюты в хэдере"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CurrencyElement(BasePage):
    CURRENCY_BTN = By.XPATH, "//ul[@class='list-inline']"

    def change_currency(self, currency:str):
        # получаем элемент кнопки выбора валюты и нажимаем
        self.click_elem(self.CURRENCY_BTN)
        # находим элемент с опцией валюты ЕВРО и нажимаем
        self.click_elem((By.XPATH, f"//a[@href={currency}]"))