"""Проверка четырех сценариев"""
import random
import pytest
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv
from pages.adm_login_page import AdmLoginPage
from pages.main_page import MainPage
from pages.prod_card_page import ProdCardPage
from pages.currency_element import CurrencyElement
from pages.cat_desktop_page import CatDesktopPage
from pages.admin_page import AdminPage
from pages.usr_reg_page import UserRegPage

load_dotenv()


class TestLoginLogoutAdministration:
    """Тестирование логина/разлогина в админке - сценарий 3.1."""

    def test_login(self, browser, get_auth_admin_url):
        """Проверка логина"""
        browser.get(get_auth_admin_url)
        # логинимся
        AdmLoginPage(browser).login()
        # Получаем элемент с именем юзера в хэдере
        el = AdmLoginPage(browser).get_element(AdmLoginPage.USERNAME_IN_HEADER)
        # Проверяем имя юзера
        assert el.text.strip(' ') == 'John Doe', 'Логин не завершился успехом'

    def test_logout(self, browser, get_auth_admin_url):
        """Проверка разлогина"""
        browser.get(get_auth_admin_url)
        # Логинимся
        AdmLoginPage(browser).login()
        # Нажимаем кнопку Logout
        AdmLoginPage(browser).click_elem(AdmLoginPage.LOGOUT_BTN)
        # Получаем элемент с заголовком формы авторизации
        el = AdmLoginPage(browser).get_element(AdmLoginPage.AUTH_FORM_TITLE)
        # Проверяем текст заголовка формы авторизации
        assert el.text == 'Please enter your login details.', 'Разлогин не завершился успехом'


class TestAddToCart:
    """Тестирование добавления товара в корзину - сценарий 3.2."""

    def test_add_to_cart(self, browser, get_base_url):
        """Проверка добавления товара в корзину"""
        browser.get(get_base_url)
        # получаем все элементы с карточками товаров на главной
        cards = MainPage(browser).get_elements(MainPage.ALL_PROD_CARDS)
        # кликаем по последней карточке с фотоаппаратом
        cards[-1].click()
        # добавляем аппарат в корзину с цветом под индексом 2 в списке опций
        ProdCardPage(browser).add_to_cart_color_select(ProdCardPage.COLOR_SELECT, 2)
        # проверяем, что на экране появляется всплывающее окно об успешном добавлении нужного товара
        ProdCardPage(browser).check_text_in_elem(ProdCardPage.CART_POP_UP, 'Canon EOS 5D')


class TestCurrChange:
    """Тестирование изменения валюты - сценарий 3.3. и 3.4."""

    def test_curr_euro_main_page(self, browser, get_base_url):
        """Проверка изменения валюты цены на главной странице на евро"""
        browser.get(get_base_url)
        # выбираем валюту EURO
        CurrencyElement(browser).change_currency("'EUR'")
        # получаем все цены с карточек товаров на главной
        prices_elems = MainPage(browser).get_elements(MainPage.ALL_PRICES)
        # проверяем, что в случайной карточке в цене на конце значок ЕВРО
        assert random.choice(prices_elems).text[-1] == '€'

    def test_curr_usd_main_page(self, browser, get_base_url):
        """Проверка изменения валюты цены на главной странице на Доллары"""
        browser.get(get_base_url)
        # выбираем валюту USD
        CurrencyElement(browser).change_currency("'USD'")
        # получаем все цены с карточек товаров на главной
        prices_elems = MainPage(browser).get_elements(MainPage.ALL_PRICES)
        # проверяем, что в случайной карточке в цене в начале значок USD
        assert random.choice(prices_elems).text[0] == '$'

    def test_curr_euro_catalog_page(self, browser, get_catalog_url):
        """Проверка изменения валюты цены на странице каталога на евро"""
        browser.get(get_catalog_url)
        # выбираем валюту EURO
        CurrencyElement(browser).change_currency("'EUR'")
        # получаем все цены с карточек товаров
        prices_elems = CatDesktopPage(browser).get_elements(CatDesktopPage.ALL_PRICES)
        # проверяем, что в случайной карточке в цене на конце значок ЕВРО
        assert random.choice(prices_elems).text[-1] == '€'

    def test_curr_usd_catalog_page(self, browser, get_catalog_url):
        """Проверка изменения валюты цены на странице каталога на Доллары"""
        browser.get(get_catalog_url)
        # выбираем валюту USD
        CurrencyElement(browser).change_currency("'USD'")
        # получаем все цены с карточек товаров
        prices_elems = CatDesktopPage(browser).get_elements(CatDesktopPage.ALL_PRICES)
        # проверяем, что в случайной карточке в цене в начале значок USD
        assert random.choice(prices_elems).text[0] == '$'


class TestAdminSite:
    """Проверки сценариев на сайте админки в рамках ДЗ №2"""

    def test_add_new_product(self, browser, get_auth_admin_url, get_base_url):
        """Проверка добавления нового продукта через админку - п.2.1 ДЗ №2"""
        browser.get(get_auth_admin_url)
        AdmLoginPage(browser).login()
        AdminPage(browser).enter_products_page()
        new_prod_dict = {
            'Product_name': f'TestProductName{"".join(random.choices("123456789", k=4))}',
            'Meta_Tag_Title': f'TestMetaTagTitle{"".join(random.choices("123456789", k=4))}',
            'Model': f'TestModel{"".join(random.choices("123456789", k=4))}',
            'Keyword': ''.join(random.choices('123456789', k=10))
        }
        AdminPage(browser).add_new_product(new_prod_dict)
        browser.get(get_base_url)
        MainPage(browser).search_for_product(new_prod_dict['Product_name'])
        MainPage(browser).search_for_elem_contains_text(new_prod_dict['Product_name'])

    def test_delete_product(self, browser, get_auth_admin_url, get_base_url):
        """Проверка удаления продукта по имени через админку - п.2.2 ДЗ №2"""
        browser.get(get_auth_admin_url)
        AdmLoginPage(browser).login()
        AdminPage(browser).enter_products_page()
        prod_name_to_delete = AdminPage(browser).get_first_line_prod_name()
        AdminPage(browser).del_product_by_name(prod_name_to_delete)
        browser.get(get_base_url)
        MainPage(browser).search_for_product(prod_name_to_delete)
        try:
            # сначала проверяем случай, когда по поиску на сайте нет никаких результатов
            MainPage(browser).search_for_elem_contains_text('There is no product that matches the search criteria.')
        except TimeoutException:
            # если поиск выдал какие-то товары, то убеждаемся, что среди них нет удаленного продукта
            elms = MainPage(browser).get_elements(MainPage.PROD_NAME_IN_CARD)
            rez = 1
            for el in elms:
                if el.text == prod_name_to_delete:
                    rez = 0
            assert rez, "Удаленный элемент найден в результатах поиска"


class TestRegUser:
    """Проверка регистрации пользователя Opencart в рамках п.2.3 ДЗ №2"""

    @pytest.mark.parametrize('params',
                             [
                                 ('', 'test',
                                  f'mail{"".join(random.choices("123456789", k=3))}@test.ru', '12345'),
                                 ('test', '',
                                  f'mail{"".join(random.choices("123456789", k=3))}@test.ru', '12345'),
                                 ('test', 'test', '', '12345'),
                                 ('test', 'test',
                                  f'mail{"".join(random.choices("123456789", k=3))}@test.ru', ''),
                                 ('test', 'test', 'mail', '12345'),
                                 ('test', 'test', 'mail@test', '12345'),
                                 ('test', 'test',
                                  f'mail{"".join(random.choices("123456789", k=3))}@test.ru', '123'),
                                 ('test', 'test',
                                  f'mail{"".join(random.choices("123456789", k=3))}@test.ru',
                                  '123456789012345678901'),
                                 ('testtesttesttesttesttesttesttesttesttest123', 'test',
                                  f'mail{"".join(random.choices("123456789", k=3))}@test.ru', '12345'),
                                 ('test', 'testtesttesttesttesttesttesttesttesttest123',
                                  f'mail{"".join(random.choices("123456789", k=3))}@test.ru', '12345'),
                             ],
                             ids=[
                                 'fname missing',
                                 'lname missing',
                                 'email missing',
                                 'password missing',
                                 '@ missing in email',
                                 'domain name missing in email',
                                 'less than 4 char in pass',
                                 'more than 20 char in pass',
                                 'more than 32 char in fname',
                                 'more than 32 char in lname',
                             ])
    def test_user_register_valid_neg(self, browser, get_user_reg_url, params):
        """Негативные проверки с невалидными данными"""
        browser.get(get_user_reg_url)
        UserRegPage(browser).reg_user(
            params[0],
            params[1],
            params[2],
            params[3]
        )
        UserRegPage(browser).click_elem(UserRegPage.MY_ACCOUNT_BTN)
        el = UserRegPage(browser).get_elements(UserRegPage.MY_ACCOUNT_OPTIONS)
        assert el[-1].text == 'Login', 'Регистрация прошла с невалидными данными'

    def test_user_register_chbx_policy_unchecked_neg(self, browser, get_user_reg_url):
        """Неготивная проверка регистрации с отключенным чек боксом I have read and agree to the Privacy Policy"""
        browser.get(get_user_reg_url)
        UserRegPage(browser).fill_reg_fields_only(
            'test',
            'test',
            f'mail{"".join(random.choices("123456789", k=4))}@test.ru',
            '12345'
        )
        UserRegPage(browser).click_elem(UserRegPage.MY_ACCOUNT_BTN)
        el = UserRegPage(browser).get_elements(UserRegPage.MY_ACCOUNT_OPTIONS)
        assert el[-1].text == 'Login', ('Регистрация прошла с отключенным чекбоксом '
                                       '"I have read and agree to the Privacy Policy"')

    def test_user_register_same_email(self, browser, get_user_reg_url):
        """Неготивная проверка регистрации с имейлом, который уже зарегистрирован"""
        browser.get(get_user_reg_url)
        test_email = f'mail{"".join(random.choices("123456789", k=4))}@test.ru'
        UserRegPage(browser).fill_reg_fields_only(
            'test',
            'test',
            test_email,
            '12345'
        )
        browser.get(get_user_reg_url)
        UserRegPage(browser).fill_reg_fields_only(
            'test2',
            'test2',
            test_email,
            '123456'
        )
        UserRegPage(browser).click_elem(UserRegPage.MY_ACCOUNT_BTN)
        el = UserRegPage(browser).get_elements(UserRegPage.MY_ACCOUNT_OPTIONS)
        assert el[-1].text == 'Login', 'Регистрация прошла с уже заргистрированным email'

    @pytest.mark.parametrize('params',
                             [
                                 ('t', 'test',
                                  f'mail{"".join(random.choices("123456789", k=6))}@test.ru', '12345'),
                                 ('test', 't',
                                  f'mail{"".join(random.choices("123456789", k=6))}@test.ru', '12345'),
                                 ('testtesttesttesttesttesttesttest', 'test',
                                  f'mail{"".join(random.choices("123456789", k=6))}@test.ru', '12345'),
                                 ('test', 'testtesttesttesttesttesttesttest',
                                  f'mail{"".join(random.choices("123456789", k=6))}@test.ru', '12345'),
                                 ('test', 'test',
                                  f'mail{"".join(random.choices("123456789", k=6))}@test.ru', '1234'),
                                 ('test', 'test',
                                  f'mail{"".join(random.choices("123456789", k=6))}@test.ru',
                                  '1234567890abcdefghij'),
                             ],
                             ids=[
                                 'fname = 1 char',
                                 'lname = 1 char',
                                 'fname = 32 chars',
                                 'lname = 32 chars',
                                 'password = 4 chars',
                                 'password = 20 chars'
                             ])
    def test_user_register_posit(self, browser, get_user_reg_url, params):
        """Позитивные проверки с валидными данными"""
        browser.get(get_user_reg_url)
        UserRegPage(browser).reg_user(
            params[0],
            params[1],
            params[2],
            params[3]
        )
        UserRegPage(browser).click_elem(UserRegPage.MY_ACCOUNT_BTN)
        els = UserRegPage(browser).get_elements(UserRegPage.MY_ACCOUNT_OPTIONS)
        assert els[-1].text == 'Logout', 'Авторизация НЕ прошла с валидными данными'

