"""Модуль проверок наличия элементов на странице карточки товара"""
from pages.prod_card_page import ProdCardPage


class TestProductCard:
    """Проверки страницы карточки товара"""
    def test_window_title(self, browser, get_apple_cinema_card_url):
        """Проверка заголовка страницы карточки товара"""
        browser.get(get_apple_cinema_card_url)
        assert browser.title == 'Apple Cinema 30'

    def test_like_button(self, browser, get_apple_cinema_card_url):
        """Проверка наличия лайк-кнопки и текста его тултипа"""
        browser.get(get_apple_cinema_card_url)
        el = ProdCardPage(browser).get_element(ProdCardPage.LIKE_BTN)
        assert el.get_attribute('title') == 'Add to Wish List'

    def test_textarea_field(self, browser, get_apple_cinema_card_url):
        """Проверка наличия текстового поля с плейсхолдером Textarea"""
        browser.get(get_apple_cinema_card_url)
        el = ProdCardPage(browser).get_element(ProdCardPage.TEXTAREA_FLD)
        assert el.get_attribute('placeholder') == 'Textarea'

    def test_add_to_cart_btn(self, browser, get_apple_cinema_card_url):
        """Проверка наличия кнопки добавления в корзину и текста в ней"""
        browser.get(get_apple_cinema_card_url)
        el = ProdCardPage(browser).get_element(ProdCardPage.ADD_TO_CART_BTN)
        assert el.text == 'Add to Cart'

    def test_tab_description(self, browser, get_apple_cinema_card_url):
        """Проверка наличия таба с описанием товара и текста заголовка этого таба"""
        browser.get(get_apple_cinema_card_url)
        el = ProdCardPage(browser).get_element(ProdCardPage.DESCR_TAB)
        assert el.text == 'Description'
