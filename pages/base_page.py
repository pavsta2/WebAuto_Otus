"""Модуль базовых методов взаимодействия с элементами"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, wait=4):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=wait)
        self.actions = ActionChains(driver)

    def get_element(self, locator: tuple):
        el = self.wait.until(EC.presence_of_element_located(locator),
                             message='No such element')
        return el

    def get_elements(self, locator: tuple):
        els = self.wait.until(EC.presence_of_all_elements_located(locator),
                              message='No such element')
        return els

    def fill_the_field(self, locator: tuple, test_data: str) -> None:
        el = self.get_element(locator)
        self.actions.move_to_element(el).pause(1).click().perform()
        el.clear()
        for i in test_data:
            el.send_keys(i)

    def click_elem(self, locator: tuple) -> None:
        el = self.get_element(locator)
        self.actions.move_to_element(el).pause(1).click().release().perform()

    def select_opt_by_ind(self, locator: tuple, index=0):
        options = Select(self.get_element(locator))
        options.select_by_index(index)

    def check_text_in_elem(self, locator: tuple, text: str):
        self.wait.until(EC.text_to_be_present_in_element(locator, text),
                        message='No such element')
        return text

    def search_for_elem_contains_text(self, text: str):
        self.get_element((By.XPATH, f"//*[contains(text(), '{text}')]"))
