"""Модуль проверок наличия элементов на страницы регистрации юзера"""
from pages.usr_reg_page import UserRegPage


class TestUserRegPage:
    """Проверки страницы регистрации юзера"""
    def test_window_title(self, browser, get_user_reg_url):
        """Проверка заголовка страницы регистрации юзера"""
        browser.get(get_user_reg_url)
        assert browser.title == 'Register Account'

    def test_reg_page_title(self, browser, get_user_reg_url):
        """Проверка наличия заголовка формы регистрации и его текста"""
        browser.get(get_user_reg_url)
        el = UserRegPage(browser).get_element(UserRegPage.REG_FORM_TITLE)
        assert el.text == 'Register Account'

    def test_fname_fld(self, browser, get_user_reg_url):
        """Проверка наличия поля ввода имени и его плейсхолдера"""
        browser.get(get_user_reg_url)
        el = UserRegPage(browser).get_element(UserRegPage.FIRSTNAME_FLD)
        assert el.get_attribute('placeholder') == 'First Name'

    def test_lname_fld(self, browser, get_user_reg_url):
        """Проверка наличия поля ввода фамилии и его плейсхолдера"""
        browser.get(get_user_reg_url)
        el = UserRegPage(browser).get_element(UserRegPage.LASTNAME_FLD)
        assert el.get_attribute('placeholder') == 'Last Name'

    def test_subscribe_chbx(self, browser, get_user_reg_url):
        """Проверка наличия чекбокса подписки"""
        browser.get(get_user_reg_url)
        el = UserRegPage(browser).get_element(UserRegPage.SUBSCR_BTN)
        assert el.get_attribute('type') == 'checkbox'

    def test_continue_btn(self, browser, get_user_reg_url):
        """Проверка наличия кнопки Continue и текста этой кнопки"""
        browser.get(get_user_reg_url)
        el = UserRegPage(browser).get_element(UserRegPage.CONTINUE_BTN)
        assert el.text == 'Continue'
