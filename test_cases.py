"""Проверка четырех сценариев"""
import os
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv

from elem_methods import fill_the_field, click_elem

load_dotenv()


class TestLoginLogoutAdministration:
    """Тестирование логина/разлогина в админке - сценарий 3.1."""

    def test_login(self, browser, get_auth_admin_url):
        """Проверка логина"""
        browser.get(get_auth_admin_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        # Заполняем поля
        fill_the_field(browser, "username", os.getenv("OPENCART_USERNAME"), 'NAME')
        fill_the_field(browser, "password", os.getenv("OPENCART_PASSWORD"), 'NAME')
        # Нажимаем кнопку Login
        click_elem(browser, "//button[@class='btn btn-primary']", 'XPATH')
        # Получаем элемент с именем юзера в хэдере
        el = wait.until(EC.presence_of_element_located((By.XPATH,
                                                        "//span[@class='d-none d-md-inline d-lg-inline']")),
                        message='No such element')
        # Проверяем имя юзера
        assert el.text.strip(' ') == 'John Doe', 'Логин не завершился успехом'

    def test_logout(self, browser, get_auth_admin_url):
        """Проверка разлогина"""
        browser.get(get_auth_admin_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)

        # Логинимся
        # Заполняем поля
        fill_the_field(browser, "username", os.getenv("OPENCART_USERNAME"), 'NAME')
        fill_the_field(browser, "password", os.getenv("OPENCART_PASSWORD"), 'NAME')
        # Нажимаем кнопку Login
        click_elem(browser, "//button[@class='btn btn-primary']", 'XPATH')

        # Нажимаем кнопку Logout
        click_elem(browser, "//a[@class='nav-link']", 'XPATH')
        # Получаем элемент с заголовком формы авторизации
        el = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "card-header")),
                        message='No such element')
        # Проверяем текст заголовка формы авторизации
        assert el.text == 'Please enter your login details.', 'Разлогин не завершился успехом'


class TestAddToCart:
    """Тестирование добавления товара в корзину - сценарий 3.2."""

    def test_add_to_cart(self, browser, get_base_url):
        """Проверка добавления товара в корзину"""
        browser.get(get_base_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        # получаем все элементы с карточками товаров на главной
        cards = wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                "//a/img[@class='img-fluid']")),
                           message='No such element')
        # кликаем по последней карточке с фотоаппаратом
        cards[-1].click()
        # получаем объект селект из поля выбора цвета аппарата
        select = Select(wait.until(EC.presence_of_element_located((By.NAME, "option[226]")),
                                   message='No such element'))
        # выбираем опцию по индексу
        select.select_by_index(2)
        # нажимаем на кнопку добавления в корзину
        click_elem(browser, '//*[@id="button-cart"]', 'XPATH')
        # проверяем, что на экране появляется всплывающее окно об успешном добавлении нужного товара
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div/div/a"), 'Canon EOS 5D'),
                   message='No such element')


class TestCurrChange:
    """Тестирование изменения валюты - сценарий 3.3. и 3.4."""

    def test_curr_euro_main_page(self, browser, get_base_url):
        """Проверка изменения валюты цены на главной странице на евро"""
        browser.get(get_base_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        # получаем элемент кнопки выбора валюты и нажимаем
        click_elem(browser, "//ul[@class='list-inline']", 'XPATH')
        # находим элемент с опцией валюты ЕВРО и нажимаем
        click_elem(browser, "//a[@href='EUR']", 'XPATH')
        # получаем все цены с карточек товаров на главной
        prices_elems = wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                       "//span[@class='price-new']")),
                                  message='No such element')
        # проверяем, что в случайной карточке в цене на конце значок ЕВРО
        assert random.choice(prices_elems).text[-1] == '€'

    def test_curr_usd_main_page(self, browser, get_base_url):
        """Проверка изменения валюты цены на главной странице на Доллары"""
        browser.get(get_base_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        # получаем элемент кнопки выбора валюты и нажимаем
        click_elem(browser, "//ul[@class='list-inline']", 'XPATH')
        # находим элемент с опцией валюты USD и нажимаем
        click_elem(browser, "//a[@href='USD']", 'XPATH')
        # получаем все цены с карточек товаров на главной
        prices_elems = wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                       "//span[@class='price-new']")),
                                  message='No such element')
        # проверяем, что в случайной карточке в цене в начале значок USD
        assert random.choice(prices_elems).text[0] == '$'

    def test_curr_euro_catalog_page(self, browser, get_catalog_url):
        """Проверка изменения валюты цены на странице каталога на евро"""
        browser.get(get_catalog_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        # получаем элемент кнопки выбора валюты и нажимаем
        click_elem(browser, "//ul[@class='list-inline']", 'XPATH')
        # находим элемент с опцией валюты ЕВРО и нажимаем
        click_elem(browser, "//a[@href='EUR']", 'XPATH')
        # получаем все цены с карточек товаров на главной
        prices_elems = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='price-new']")),
                                  message='No such element')
        # проверяем, что в случайной карточке в цене на конце значок ЕВРО
        assert random.choice(prices_elems).text[-1] == '€'

    def test_curr_usd_catalog_page(self, browser, get_catalog_url):
        """Проверка изменения валюты цены на странице каталога на Доллары"""
        browser.get(get_catalog_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        # получаем элемент кнопки выбора валюты и нажимаем
        click_elem(browser, "//ul[@class='list-inline']", 'XPATH')
        # находим элемент с опцией валюты USD и нажимаем
        click_elem(browser, "//a[@href='USD']", 'XPATH')
        # получаем все цены с карточек товаров на главной
        prices_elems = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='price-new']")),
                                  message='No such element')
        # проверяем, что в случайной карточке в цене в начале значок USD
        assert random.choice(prices_elems).text[0] == '$'
