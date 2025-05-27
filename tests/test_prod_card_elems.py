"""Модуль проверок наличия элементов на странице карточки товара"""
import allure
from selenium.common.exceptions import TimeoutException
from pages.prod_card_page import ProdCardPage


@allure.feature("Проверки страницы карточки продукта")
class TestProductCard:
    """Проверки страницы карточки товара"""
    @allure.title("Проверка заголовка страницы карточки товара")
    def test_window_title(self, browser, get_macbook_card_url):
        """Проверка заголовка страницы карточки товара"""
        ProdCardPage(browser).open(get_macbook_card_url)
        assert browser.title == 'MacBook'

    @allure.title("Проверка наличия лайк-кнопки и текста его тултипа")
    def test_like_button(self, browser, get_macbook_card_url):
        """Проверка наличия лайк-кнопки и текста его тултипа"""
        ProdCardPage(browser).open(get_macbook_card_url)
        el = ProdCardPage(browser).get_element(ProdCardPage.LIKE_BTN)
        assert el.get_attribute('title') == 'Add to Wish List'

    @allure.title("Проверка наличия текстового поля с плейсхолдером Textarea")
    def test_textarea_field(self, browser, get_macbook_card_url):
        """Проверка наличия текстового поля с плейсхолдером Textarea"""
        ProdCardPage(browser).open(get_macbook_card_url)
        el = ProdCardPage(browser).get_element(ProdCardPage.TEXTAREA_FLD)
        assert el.get_attribute('placeholder') == 'Textarea'

    @allure.title("Проверка наличия кнопки добавления в корзину и текста в ней")
    def test_add_to_cart_btn(self, browser, get_macbook_card_url):
        """Проверка наличия кнопки добавления в корзину и текста в ней"""
        ProdCardPage(browser).open(get_macbook_card_url)
        el = ProdCardPage(browser).get_element(ProdCardPage.ADD_TO_CART_BTN)
        assert el.text == 'Add to Cart'

    @allure.title("Проверка наличия таба с описанием товара и текста заголовка этого таба")
    def test_tab_description(self, browser, get_macbook_card_url):
        """Проверка наличия таба с описанием товара и текста заголовка этого таба"""
        ProdCardPage(browser).open(get_macbook_card_url)
        el = ProdCardPage(browser).get_element(ProdCardPage.DESCR_TAB)
        assert el.text == 'Description'
