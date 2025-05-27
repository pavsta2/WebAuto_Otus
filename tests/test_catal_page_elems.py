"""Модуль проверок наличия элементов на странице каталога"""
import allure
import pytest
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from pages.cat_desktop_page import CatDesktopPage


@allure.feature("Проверки страницы каталога")
class TestCatalogDesktopsPage:
    """Проверки страницы каталога Desktops"""
    @allure.title("Проверка заголовка окна страницы каталога Desktops")
    def test_window_title(self, browser, get_catalog_url):
        """Проверка заголовка окна страницы каталога Desktops"""
        CatDesktopPage(browser).open(get_catalog_url)
        assert browser.title == 'Desktops'

    @allure.title("Проверка заголовка раздела каталога")
    def test_catalog_title(self, browser, get_catalog_url):
        """Проверка заголовка раздела каталога"""
        CatDesktopPage(browser).open(get_catalog_url)
        el = CatDesktopPage(browser).get_element(CatDesktopPage.CATALOG_TITLE)
        assert el.text == 'Desktops'

    @allure.title("Проверка наличия селект-поля с опциями сортировки и наименования этих опций ({param_id})")
    @pytest.mark.parametrize('test_opt_list',
                             [['Default',
                               'Name (A - Z)',
                               'Name (Z - A)',
                               'Price (Low > High)',
                               'Price (High > Low)',
                               'Rating (Highest)',
                               'Rating (Lowest)',
                               'Model (A - Z)',
                               'Model (Z - A)']],
                             ids=['valid option list'])
    def test_sort_select_field(self, browser, get_catalog_url, test_opt_list):
        """Проверка наличия селект-поля с опциями сортировки и наименования этих опций"""
        CatDesktopPage(browser).open(get_catalog_url)
        el = CatDesktopPage(browser).get_element(CatDesktopPage.SELECT_SORT_FLD)
        opt_list = []
        for option in Select(el).options:
            opt_list.append(option.text)
        assert opt_list == test_opt_list

    @allure.title("Проверка наличия селекта с опциями ограничения кол-ва эл-ов на странице "
                  "и наименования этих опций ({param_id})")
    @pytest.mark.parametrize('test_opt_list',
                             [['10',
                               '25',
                               '50',
                               '75',
                               '100']],
                             ids=['valid option list'])
    def test_show_limit_select_field(self, browser, get_catalog_url, test_opt_list):
        """Проверка наличия селект-поля с опциями ограничения кол-ва эл-ов на странице и наименования этих опций"""
        CatDesktopPage(browser).open(get_catalog_url)
        el = CatDesktopPage(browser).get_element(CatDesktopPage.SELECT_LIMIT_FLD)
        opt_list = []
        for option in Select(el).options:
            opt_list.append(option.text)
        assert opt_list == test_opt_list

    @allure.title("Проверка наличия панели breadcrumb и наимен-ния текущего местоположения (последнего элемента)")
    def test_breadcrumb_bar(self, browser, get_catalog_url):
        """Проверка наличия панели breadcrumb и наименования текущего местоположения (последнего элемента)"""
        CatDesktopPage(browser).open(get_catalog_url)
        el = CatDesktopPage(browser).get_elements(CatDesktopPage.BRDCRUMBS_ELEM)
        assert el[-1].text == 'Desktops'
