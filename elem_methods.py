"""Модуль методов взаимодействия с элементами"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fill_the_field(browser, field_locator: str, test_data: str, find_meth: str) -> None:
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    el = None
    if find_meth == 'CSS_SELECTOR':
        el = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, field_locator)),
                        message='No such element')
    elif find_meth == 'XPATH':
        el = wait.until(EC.presence_of_element_located((By.XPATH, field_locator)),
                        message='No such element')
    el.clear()
    el.click()
    el.send_keys(test_data)


def click_elem(browser, field_locator: str, find_meth: str) -> None:
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    el = None
    if find_meth == 'CSS_SELECTOR':
        el = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, field_locator)),
                        message='No such element')
    elif find_meth == 'XPATH':
        el = wait.until(EC.presence_of_element_located((By.XPATH, field_locator)),
                        message='No such element')
    el.click()
