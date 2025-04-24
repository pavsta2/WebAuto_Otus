"""Модуль методов взаимодействия с элементами"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fill_the_field(browser, field_locator: str, test_data: str, find_meth: str) -> None:
    """Функция для заполнения поля"""
    wait = WebDriverWait(browser, 5, poll_frequency=1)

    if find_meth == 'CLASS_NAME':
        el = wait.until(EC.presence_of_element_located((By.CLASS_NAME, field_locator)),
                        message='No such element')
        el.clear()
        el.click()
        el.send_keys(test_data)
    elif find_meth == 'ID':
        el = wait.until(EC.presence_of_element_located((By.ID, field_locator)),
                        message='No such element')
        el.clear()
        el.click()
        el.send_keys(test_data)
    elif find_meth == 'NAME':
        el = wait.until(EC.presence_of_element_located((By.NAME, field_locator)),
                        message='No such element')
        el.clear()
        el.click()
        el.send_keys(test_data)
    elif find_meth == 'XPATH':
        el = wait.until(EC.presence_of_element_located((By.XPATH, field_locator)),
                        message='No such element')
        el.clear()
        el.click()
        el.send_keys(test_data)


def click_elem(browser, field_locator: str, find_meth: str) -> None:
    """Функция клика по элементу"""
    wait = WebDriverWait(browser, 5, poll_frequency=1)

    if find_meth == 'CLASS_NAME':
        el = wait.until(EC.presence_of_element_located((By.CLASS_NAME, field_locator)),
                        message='No such element')
        el.click()
    elif find_meth == 'ID':
        el = wait.until(EC.presence_of_element_located((By.ID, field_locator)),
                        message='No such element')
        el.click()
    elif find_meth == 'NAME':
        el = wait.until(EC.presence_of_element_located((By.NAME, field_locator)),
                        message='No such element')
        el.click()
    elif find_meth == 'XPATH':
        el = wait.until(EC.presence_of_element_located((By.XPATH, field_locator)),
                        message='No such element')
        el.click()
