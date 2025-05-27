"""Модуль проверок наличия элементов на главной странице"""
import allure
import pytest
from pages.main_page import MainPage
from selenium.common.exceptions import TimeoutException


@allure.feature("Проверки главной страницы")
class TestMainPage:
    """Проверки главной страницы"""

    @allure.title("Проверка заголовка окна главной страницы")
    def test_window_title(self, browser, get_base_url):
        """Проверка заголовка окна главной страницы"""
        MainPage(browser).open(get_base_url)
        assert browser.title == 'Your Store'

    @allure.title("Проверка наличия компонента навигации карусели")
    def test_carousel_presence(self, browser, get_base_url):
        """Проверка наличия компонента навигации карусели"""
        MainPage(browser).open(get_base_url)
        MainPage(browser).get_element(MainPage.CAROUSEL_EL)


    @allure.title("Проверка наличия поискового поля и текста плейсхолдера в нем")
    def test_search_field(self, browser, get_base_url):
        """Проверка наличия поискового поля и текста плейсхолдера в нем"""
        MainPage(browser).open(get_base_url)
        el = MainPage(browser).get_element(MainPage.SEARCH_FIELD)
        assert el.get_attribute('placeholder') == 'Search'

    @allure.title("Проверка наличия кнопки корзины и текста в ней")
    def test_header_cart_button(self, browser, get_base_url):
        """Проверка наличия кнопки корзины и текста в ней"""
        MainPage(browser).open(get_base_url)
        el = MainPage(browser).get_element(MainPage.CART_BTN)
        assert el.text == '0 item(s) - $0.00'

    @allure.title("Проверка наличия панели с кнопками каталога и наименований этих кнопок ({param_id})")
    @pytest.mark.parametrize('test_button_list',
                             [['Desktops',
                               'Laptops & Notebooks',
                               'Components',
                               'Tablets',
                               'Software',
                               'Phones & PDAs',
                               'Cameras',
                               'MP3 Players']],
                             ids=['valid option list'])
    def test_nav_bar(self, browser, get_base_url, test_button_list):
        """Проверка наличия панели с кнопками каталога и наименований этих кнопок"""
        MainPage(browser).open(get_base_url)
        els = MainPage(browser).get_elements(MainPage.NAV_PANEL)
        tabs_list = []
        for i in els:
            tabs_list.append(i.text)
        assert tabs_list == test_button_list
