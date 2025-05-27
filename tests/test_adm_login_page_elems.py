"""Модуль проверок наличия элементов на странице авторизации в админку"""
import allure
from selenium.common.exceptions import TimeoutException
from pages.adm_login_page import AdmLoginPage


@allure.feature("Проверки админки")
class TestAdminLoginPage:
    """Проверки страницы авторизации в админку"""
    @allure.title("Проверка заголовка страницы авторизации в админку")
    def test_window_title(self, browser, get_auth_admin_url):
        """Проверка заголовка страницы авторизации в админку"""
        AdmLoginPage(browser).open(get_auth_admin_url)
        assert browser.title == 'Administration'

    @allure.title("Проверка наличия заголовка формы авторизации и его текста")
    def test_title_auth(self, browser, get_auth_admin_url):
        """Проверка наличия заголовка формы авторизации и его текста"""
        AdmLoginPage(browser).open(get_auth_admin_url)
        el = AdmLoginPage(browser).get_element(AdmLoginPage.AUTH_FORM_TITLE)
        assert el.text == 'Please enter your login details.'

    @allure.title("Проверка наличия заголовка поля юзернейма и его текста")
    def test_username_fld_title(self, browser, get_auth_admin_url):
        """Проверка наличия заголовка поля юзернейма и его текста"""
        AdmLoginPage(browser).open(get_auth_admin_url)
        el = AdmLoginPage(browser).get_element(AdmLoginPage.USERNAME_FLD_TITLE)
        assert el.text == 'Username'

    @allure.title("Проверка наличия заголовка поля пароля и его текста")
    def test_pass_fld_title(self, browser, get_auth_admin_url):
        """Проверка наличия заголовка поля пароля и его текста"""
        AdmLoginPage(browser).open(get_auth_admin_url)
        el = AdmLoginPage(browser).get_element(AdmLoginPage.PASS_FLD_TITLE)
        assert el.text == 'Password'

    @allure.title("Проверка наличия поля ввода юзернейма и его плейсхолдера")
    def test_username_fld(self, browser, get_auth_admin_url):
        """Проверка наличия поля ввода юзернейма и его плейсхолдера"""
        AdmLoginPage(browser).open(get_auth_admin_url)
        el = AdmLoginPage(browser).get_element(AdmLoginPage.USERNAME_FLD)
        assert el.get_attribute('placeholder') == 'Username'

    @allure.title("Проверка наличия поля ввода пароля и его плейсхолдера")
    def test_pass_fld(self, browser, get_auth_admin_url):
        """Проверка наличия поля ввода пароля и его плейсхолдера"""
        AdmLoginPage(browser).open(get_auth_admin_url)
        el = AdmLoginPage(browser).get_element(AdmLoginPage.PASS_FLD)
        assert el.get_attribute('placeholder') == 'Password'
