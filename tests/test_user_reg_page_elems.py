"""Модуль проверок наличия элементов на страницы регистрации юзера"""
import allure
from selenium.common.exceptions import TimeoutException
from pages.usr_reg_page import UserRegPage


@allure.feature("Проверки страницы регистрации пользователя")
class TestUserRegPage:
    """Проверки страницы регистрации юзера"""
    @allure.title("Проверка заголовка страницы регистрации юзера")
    def test_window_title(self, browser, get_user_reg_url):
        """Проверка заголовка страницы регистрации юзера"""
        UserRegPage(browser).open(get_user_reg_url)
        assert browser.title == 'Register Account'

    @allure.title("Проверка наличия заголовка формы регистрации и его текста")
    def test_reg_page_title(self, browser, get_user_reg_url):
        """Проверка наличия заголовка формы регистрации и его текста"""
        UserRegPage(browser).open(get_user_reg_url)
        el = UserRegPage(browser).get_element(UserRegPage.REG_FORM_TITLE)
        assert el.text == 'Register Account'

    @allure.title("Проверка наличия поля ввода имени и его плейсхолдера")
    def test_fname_fld(self, browser, get_user_reg_url):
        """Проверка наличия поля ввода имени и его плейсхолдера"""
        UserRegPage(browser).open(get_user_reg_url)
        el = UserRegPage(browser).get_element(UserRegPage.FIRSTNAME_FLD)
        assert el.get_attribute('placeholder') == 'First Name'

    @allure.title("Проверка наличия поля ввода фамилии и его плейсхолдера")
    def test_lname_fld(self, browser, get_user_reg_url):
        """Проверка наличия поля ввода фамилии и его плейсхолдера"""
        UserRegPage(browser).open(get_user_reg_url)
        el = UserRegPage(browser).get_element(UserRegPage.LASTNAME_FLD)
        assert el.get_attribute('placeholder') == 'Last Name'

    @allure.title("Проверка наличия чекбокса подписки")
    def test_subscribe_chbx(self, browser, get_user_reg_url):
        """Проверка наличия чекбокса подписки"""
        UserRegPage(browser).open(get_user_reg_url)
        el = UserRegPage(browser).get_element(UserRegPage.SUBSCR_BTN)
        assert el.get_attribute('type') == 'checkbox'

    @allure.title("Проверка наличия кнопки Continue и текста этой кнопки")
    def test_continue_btn(self, browser, get_user_reg_url):
        """Проверка наличия кнопки Continue и текста этой кнопки"""
        UserRegPage(browser).open(get_user_reg_url)
        el = UserRegPage(browser).get_element(UserRegPage.CONTINUE_BTN)
        assert el.text == 'Continue'
