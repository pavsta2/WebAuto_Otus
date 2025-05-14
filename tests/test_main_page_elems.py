"""Модуль проверок наличия элементов на главной странице"""
import pytest
from pages.main_page import MainPage


class TestMainPage:
    """Проверки главной страницы"""
    def test_window_title(self, browser, get_base_url):
        """Проверка заголовка окна главной страницы"""
        browser.get(get_base_url)
        assert browser.title == 'Your Store'

    def test_carousel_presence(self, browser, get_base_url):
        """Проверка наличия компонента навигации карусели"""
        browser.get(get_base_url)
        MainPage(browser).get_element(MainPage.CAROUSEL_EL)

    def test_search_field(self, browser, get_base_url):
        """Проверка наличия поискового поля и текста плейсхолдера в нем"""
        browser.get(get_base_url)
        el = MainPage(browser).get_element(MainPage.SEARCH_FIELD)
        assert el.get_attribute('placeholder') == 'Search'

    def test_header_cart_button(self, browser, get_base_url):
        """Проверка наличия кнопки корзины и текста в ней"""
        browser.get(get_base_url)
        el = MainPage(browser).get_element(MainPage.CART_BTN)
        assert el.text == '0 item(s) - $0.00'

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
        browser.get(get_base_url)
        els = MainPage(browser).get_elements(MainPage.NAV_PANEL)
        tabs_list = []
        for i in els:
            tabs_list.append(i.text)
        assert tabs_list == test_button_list
